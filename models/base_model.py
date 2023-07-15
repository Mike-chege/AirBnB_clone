#!/usr/bin/python3
"""
This BaseModel class defines all common
attributes/methods for other classes
"""


from uuid import uuid4
import datetime
import models


class BaseModel():
    """
    BaseModel class defines methods/attributes
    for all other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing *args and **kwargs
        """
        if len(kwargs) >= 1:
            self.inst_to_dict(**kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints class name, self.id, self.__dict__
        """
        m_str = "["
        m_str += str(self.__class__.__name__) + '] ('
        m_str += str(self.id) + ') ' + str(self.__dict__)
        return m_str

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_inst = self.__dict__.copy()
        dict_inst['__class__'] = self.__class__.__name__
        dict_inst['created_at'] = self.created_at.isoformat()
        dict_inst['updated_at'] = self.updated_at.isoformat()
        return dict_inst

    def inst_to_dict(self, **kwargs):
        """
        converts dictionaries back to instances
        """
        for (k, v) in kwargs.items():
            if k in ('created_at', 'updated_at'):
                self.__dict__[k] = datetime.datetime\
                        .strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[k] = v
