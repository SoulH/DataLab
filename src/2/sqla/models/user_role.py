from .base import *


user_role_association_table = Table(
    'user_role_association_table',
    Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('role_id', ForeignKey('role.id'), primary_key=True)
)