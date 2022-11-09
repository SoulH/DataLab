from core.data.repository import IRepository
from .base import map_filters, session_maker, to_dict


class SQLARepository(IRepository):
    def __init__(self, model: type, session = None):
        self.typ = model
        self.session = session or session_maker()

    def __query__(self, **kwargs):
        fil = map_filters(self.typ, **kwargs)
        return self.session.query(self.typ).filter(*fil)

    def find(self, query: dict = {}, sort: list = ['-id'], page: int = None, page_size: int = 10, **kwargs):
        q = self.__query__(**(query or kwargs))
        return list(map(to_dict, q.all()))

    def first(self, query: dict = {}, sort: list = ['-id'], **kwargs):
        res = self.__query__(**(query or kwargs)).first()
        return to_dict(res) if res else None

    def last(self, query: dict = {}, sort: list = ['-id'], **kwargs):
        res = self.__query__(**(query or kwargs)).last()
        return to_dict(res) if res else None
    
    def exists(self, query: dict = {}, **kwargs) -> bool:
        return len(self.__query__(**(query or kwargs)).all()) > 0
    
    def upsert(self, data: dict | list[dict], query: dict = None):
        def fn(d: dict, e=None):
            if not e and d.get('id', 0):
                e = self.__query__(id=d['id']).first()
            kwargs = {**to_dict(e), **d} if e else d
            ed = self.typ(**kwargs)
            return to_dict(self.session.merge(ed))
        if isinstance(data, dict):
            if not query:
                return fn(data)
            q = self.__query__(**query)
            return [fn(data, e) for e in q.all()]
        return list(map(fn, data))
    
    def delete(self, query: dict = ..., **kwargs):
        li = self.__query__(**(query or kwargs)).all()
        if not li:
            return
        [self.session.delete(e) for e in li]

