from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def find(self, query: dict = {}, sort: list = ['id'], page: int = None, page_size: int = 10, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def first(self, query: dict = {}, sort: list = ['id'], **kwargs):
        raise NotImplementedError()
        
    @abstractmethod
    def last(self, query: dict = {}, sort: list = ['id'], **kwargs):
        raise NotImplementedError()
        
    @abstractmethod
    def exists(self, query: dict = {}, **kwargs) -> bool:
        raise NotImplementedError()
        
    @abstractmethod
    def upsert(self, data: dict|list[dict], query: dict = None):
        raise NotImplementedError()
        
    @abstractmethod
    def delete(self, query: dict = {}, **kwargs):
        raise NotImplementedError()