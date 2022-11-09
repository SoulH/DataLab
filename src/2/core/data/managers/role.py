from abc import abstractmethod
from ..repository import IRepository

class IRoleManager(IRepository):
    @abstractmethod
    def user_roles(self):
        raise NotImplementedError()