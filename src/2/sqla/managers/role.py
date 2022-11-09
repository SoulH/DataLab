from functools import reduce
from sqla.base import to_dict
from ..models.role import Role
from ..repository import SQLARepository
from core.data.managers.role import IRoleManager
from sqlalchemy.orm import joinedload


class RoleManager(SQLARepository, IRoleManager):
    def __init__(self, db) -> None:
        super().__init__(Role, db.session)
        self.db = db

    def user_roles(self):
        return self.db.users.user_roles()