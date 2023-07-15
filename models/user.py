#!/usr/bin/python3
"""
Class User with several public class attributes
And
inherits from BaseModel
"""


import uuid
from models.base_model import BaseModel
import datetime


class User(BaseModel):
    """
    Class User definition
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation method for class User
        """
        super().__init__(*args, **kwargs)
