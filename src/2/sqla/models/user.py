from .base import *
from .user_role import user_role_association_table


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    profile_picture = Column(String)
    user_full_name = Column(String)
    roles = relationship('Role', secondary=user_role_association_table, back_populates='users')