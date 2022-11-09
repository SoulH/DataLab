from core.data.managers.user import IUserManager
from sqla.base import to_dict
from sqla.repository import SQLARepository
from sqla.models.user import User
from sqlalchemy.orm import joinedload
from functools import reduce


class UserManager(SQLARepository, IUserManager):
    def __init__(self, db):
        super().__init__(User, db.session)
        self.db = db

    def user_roles(self):
        def mapper(e, fk):
            return {**to_dict(e, exclude=['id']), fk: e.id}
        def join(a, li):
            return [{**a, **mapper(b, 'role_id')} for b in li]
        def reducer(a, b):
            c = mapper(b, 'user_id')
            li = c.pop('roles', [])
            return a + join(c, li)
        q = self.__query__()
        q = q.options(joinedload(User.roles)).all()
        return reduce(reducer, q, [])
