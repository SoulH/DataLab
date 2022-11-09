from .base import *


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    project_images = Column(JSON)
    project_description = Column(Text)
    project_name = Column(String)
    project_active = Column(Boolean)