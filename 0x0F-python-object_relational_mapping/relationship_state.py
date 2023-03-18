#!/usr/bin/python3
"""
SQLAlchemy State Model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class representation of the State table of mysql database
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')
