#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = "cities"
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")
    else:
        state_id = ""
        name = ""
