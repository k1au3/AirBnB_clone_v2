#!/usr/bin/python3

""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = (models.storage.all(City))
            for city in list(all_cities.values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
