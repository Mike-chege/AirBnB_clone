#!/usr/bin/python3
"""
Class Amenity inherits from
BaseModel
"""
import uuid
from models.base_model import BaseModel
import datetime


class Amenity(BaseModel):
    """
    Class Amenity definition
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        super().__init__(*args, **kwargs)
