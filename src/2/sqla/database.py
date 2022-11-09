from core.data.database import IDatabase
from sqla.base import session_maker
from sqla.managers.project import ProjectManager
from sqla.managers.role import RoleManager
from sqla.managers.user import UserManager


class SQLADatabase(IDatabase):
    def __init__(self, session = None) -> None:
        self.session = session or session_maker()
        self._users: UserManager = None
        self._projects: ProjectManager = None
        self._roles: RoleManager = None

    @property
    def users(self) -> UserManager:
        if not self._users:
            self._users = UserManager(self)
        return self._users

    @property
    def projects(self) -> ProjectManager:
        if not self._projects:
            self._projects = ProjectManager(self)
        return self._projects

    @property
    def roles(self) -> RoleManager:
        if not self._roles:
            self._roles = RoleManager(self)
        return self._roles

    def commit(self):
        self.session.commit()