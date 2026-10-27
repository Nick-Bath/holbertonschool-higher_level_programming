#!/usr/bin/python3

"""Creating a base State class that connects to the data base"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a row of the states table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False, )