#!/usr/bin/python3
"""
State Model
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class representation of the State table of mysql database
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
