#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """
    User class inherits from BaseModel
    """
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship('Place', passive_deletes=True, backref='user')
        reviews = relationship('Review', passive_deletes=True, backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
