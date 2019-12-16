#!/usr/bin/python3
"""
 class definition of a State
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Definition of state class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement="auto")

    name = Column(String(128), nullable=False)
