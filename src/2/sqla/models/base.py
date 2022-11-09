from sqlalchemy import Integer, String, JSON, Column, Boolean, Text, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()