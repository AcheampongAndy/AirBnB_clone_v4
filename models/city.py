#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """
    Initializing a new City

    Paramets:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

        places = relationship("Place", backref="cities")
    else:
        name = ''
        state_id = ''
