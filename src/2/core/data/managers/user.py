from abc import abstractmethod
from ..repository import IRepository


class IUserManager(IRepository):
    @abstractmethod
    def user_roles(self):
        raise NotImplementedError()