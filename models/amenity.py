#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Table, ForeignKey
from os import getenv

class Amenity(BaseModel, Base):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

    else:
        name = ""
