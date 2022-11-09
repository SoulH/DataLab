from core.data.managers.project import IProjectManager
from sqla.models.project import Project
from sqla.repository import SQLARepository


class ProjectManager(SQLARepository, IProjectManager):
    def __init__(self, db):
        super().__init__(Project, db.session)
        self.db = db