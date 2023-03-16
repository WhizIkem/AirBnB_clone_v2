#!/usr/bin/python3

""" This is a file that contains the BaseModel class for other classes """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    The BaseModel class for the project
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of the base class
        """

        from models import storage

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of an object
        Format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """

        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance
        + by using self.__dict__, only instance attributes set will be returned
        + a key __class__ must be added to this dictionary with the class name
        of the object
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                dictionary[key] = value

        return dictionary
