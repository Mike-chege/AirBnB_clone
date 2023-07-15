#!/usr/bin/python3
"""
Defining the Storage variable
"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
