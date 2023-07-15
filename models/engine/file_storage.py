#!/usr/bin/python3
"""
Class FileStorage Definition
"""


# The imported modules
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class FileStorage():
    """
    Class FileStorage that serializes
    Instances to a JSON file
    And deserializes JSON file to instances:
    """
    # Engine directory declaration
    engine_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.getcwd()
    # getting the file path
    __file_path = parent_directory + '/file.json'
    __objects = dict()

    def __init__(self):
        """
        Instantiation
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        try:
            obj_d = obj.to_dict()
        except TypeError:
            print('object passed to filestorage has no to_dict()')
        key = obj_d['__class__'] + '.' + str(obj_d['id'])
        self.__objects[key] = obj

    def delete(self, obj):
        """
        Deletes objects from __objects
        """
        if obj is None or not hasattr(obj, 'id'):
            return False

        key = obj.__class__.__name__ + '.' + str(obj.id)
        try:
            del self.__objects[key]
            return True
        except KeyError:
            return False

    def save(self):
        """
        serializes __objects to the
        JSON file (path: __file_path
        """
        json_dump = str({k: v.to_dict() for (k, v) in self.__objects.items()})
        json_dump = json_dump.replace('\'', '"')
        with open(self.__file_path, 'w', encoding='utf-8') as myFile:
            myFile.write(json_dump)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except FileNotFoundError:
            return
        objects = eval(my_obj_dump)
        for (k, v) in objects.items():
            objects[k] = eval(k.split('.')[0] + '(**v)')
        self.__objects = objects

    def filePath(self):
        """
        Returns the filePath
        for the JSON file
        """
        return self.__file_path
