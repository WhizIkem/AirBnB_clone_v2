#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    """if getenv('HBNB_TYPE_STORAGE') != 'db':"""
    if models.storage_type == 'file':
        @property
        def cities(self):
            """Returns the last of City objects linked to the current State"""
            list_city = []
            for city in models.storage.all(models.City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
