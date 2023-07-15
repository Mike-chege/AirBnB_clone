#!/usr/bin/python3
"""
Class City inherits from BaseModel
"""


import uuid
from models.base_model import BaseModel
import datetime


class City(BaseModel):
    """
    Class City definition
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation method for class City
        """
        super().__init__(*args, **kwargs)
