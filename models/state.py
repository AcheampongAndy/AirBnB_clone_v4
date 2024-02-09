#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True,
                              backref="state")

    else:
        name = ''

        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of City
            with state_id equals to the current State.id
            """
            from models import storage
            cities_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
