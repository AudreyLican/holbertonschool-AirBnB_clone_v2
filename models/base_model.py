#!/usr/bin/python3
"""This module defines a class BaseModel"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """Define new class attributes"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Method to initialize a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            dformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, dformat))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Method to return a string representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop("_sa_instance_state", None)
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, dictionary)

    def save(self):
        """Method to update the attribute updated_at"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Method to return a dictionary reprst of the instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Method to delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
