#!/usr/bin/python3
"""
Unittest for filestorage.py
"""

import datetime
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """test class for testing file storage
    """
    temp_file = ""

    @staticmethod
    def move_file(source, dest):
        with open(source, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tempFile:
                tempFile.write(myFile.read())
        os.remove(source)

    def setUp(self):
        self.temp_file = storage.parent_directory + '/temp_store.json'
        self.move_file(storage.filePath(), self.temp_file)
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        self.move_file(self.temp_file, storage.filePath())
        del self.temp_objs

    def test_type(self):
        """
        Test for checking type FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """
        Test for save  command for FileStorage
        """
        with open(storage.filePath(), 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except KeyError:
            pass

    def test_reload(self):
        """
        Test for reload command for FileStorage
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except KeyError:
            pass

    def test_delete_b(self):
        """
        Test for delete comand for FileStorage
        """
        self.assertEqual(storage.delete(BaseModel()), True)
        self.assertEqual(storage.delete(self.temp_objs[2]), True)
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        with self.assertRaises(KeyError):
            obj_d[key2]

    def test_delete_wrong_input(self):
        """
        Test for delete wrong Input command for FileStorage
        """
        self.assertEqual(storage.delete(None), False)
        self.assertEqual(storage.delete('mymodel'), False)

    def test_new_b(self):
        """
        Test for new basic command for FileStorage
        """
        obj = BaseModel()
        storage.new(obj)
        obj_d = storage.all()
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.assertEqual(obj_d[key] is obj, True)

    def test_new_wrong_input(self):
        """
        Test for WrongInput command for FileStorage
        """
        try:
            self.assertRaises(storage.new('mlsjioa'), TypeError)
            self.assertRaises(storage.new(None), TypeError)
        except AttributeError:
            pass
