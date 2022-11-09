from .base import *
from .user_role import user_role_association_table


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    users = relationship('User', secondary=user_role_association_table, back_populates='roles')