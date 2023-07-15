#!/usr/bin/python3
"""
Class Review inherits from BaseModel
"""


import uuid
from models.base_model import BaseModel
import datetime


class Review(BaseModel):
    """
    Class Review definition
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation method for class Review
        """
        super().__init__(*args, **kwargs)
