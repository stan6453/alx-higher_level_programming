#!/usr/bin/python3
"""
SQLAlchemy City Model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    A class representation of the City table of mysql database
    """
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
