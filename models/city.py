#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import state
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


storage_type = os.getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and namee """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    if storage_type == 'db':
        state = relationship("State", back_populates="cities")
