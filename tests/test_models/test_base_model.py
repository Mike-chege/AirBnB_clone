#!/usr/bin/python3
"""
Unittest for base_model.py
"""


from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test for the BaseModel class
    """
    def setUp(self):
        self.temp_b = BaseModel()

    def tearDown(self):
        self.temp_b = None

    def test_type_base(self):
        """
        Test the type of base model
        """
        self.assertIsInstance(self.temp_b, BaseModel)
        self.assertEqual(type(self.temp_b), BaseModel)

    def test_basic_attribute(self):
        """
        Test for basic attributes methods
        """
        self.temp_b.name = "michael"
        self.temp_b.xyz = 400
        self.assertEqual(self.temp_b.name, "michael")
        self.assertEqual(self.temp_b.xyz, 400)

    def test_return_string(self):
        """
        Test for the string return value
        """
        my_str = str(self.temp_b)
        id_test = "[BaseModel] ({})".format(self.temp_b.id)
        boolean = id_test in my_str
        self.assertEqual(True, boolean)
        boolean = "updated_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "created_at" in my_str
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in my_str
        self.assertEqual(True, boolean)

    def test_to_dict(self):
        """
        Test for the to_dict
        """
        my_dict = self.temp_b.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.temp_b.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.temp_b.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.temp_b.__class__.__name__)
        self.assertEqual(my_dict['id'], self.temp_b.id)

    def test_to_dict_n(self):
        """
        Test for the to_dict/ datetime format
        """
        my_dict = self.temp_b.to_dict()
        created_at = my_dict['created_at']
        time = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.temp_b.created_at, time)

    def test_from_dict_s(self):
        """
        Test for the from_dict method
        """
        my_dict = self.temp_b.to_dict()
        my_base = BaseModel(**my_dict)
        self.assertEqual(my_base.id, self.temp_b.id)
        self.assertEqual(my_base.updated_at, self.temp_b.updated_at)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)
        self.assertEqual(my_base.__class__.__name__,
                         self.temp_b.__class__.__name__)

    def test_from_dict(self):
        """
        Test for the from_dict method
        """
        self.temp_b.random = "hello!"
        self.temp_b.z = 55
        my_dict = self.temp_b.to_dict()
        self.assertEqual(my_dict['z'], 55)
        my_base = BaseModel(**my_dict)
        self.assertEqual(my_base.z, self.temp_b.z)
        self.assertEqual(my_base.random, self.temp_b.random)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)

    def test_unique_id(self):
        """
        Test for the unique ids
        """
        another = BaseModel()
        another2 = BaseModel()
        self.assertNotEqual(self.temp_b.id, another.id)
        self.assertNotEqual(self.temp_b.id, another2.id)

    def test_id_type(self):
        """
        Test id type checks if it is a string
        """
        self.assertEqual(type(self.temp_b.id), str)

    def test_time_updated(self):
        """
        Time update test
        """
        time1 = self.temp_b.updated_at
        self.temp_b.save()
        time2 = self.temp_b.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime.datetime)
