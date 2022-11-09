from abc import ABC, abstractmethod
from .managers.project import IProjectManager
from .managers.user import IUserManager


class IDatabase(ABC):
    @property
    @abstractmethod
    def users(self) -> IUserManager:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def projects(self) -> IProjectManager:
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()