#!/usr/bin/python3
"""
Unittest for state.py
"""


from models.base_model import BaseModel
from models.state import State
import datetime
import unittest


class TestStateModel(unittest.TestCase):
    """
    Class TestStateModel definition
    """
    def setUp(self):
        self.temp_b = State()

    def tearDown(self):
        self.temp_b = None

    def test_type(self):
        """
        Test for the type of state model
        """
        self.assertIsInstance(self.temp_b, State)
        self.assertEqual(type(self.temp_b), State)
        self.assertEqual(issubclass(self.temp_b.__class__, BaseModel), True)
        self.assertEqual(isinstance(self.temp_b, BaseModel), True)

    def test_name_type(self):
        """
        Test for the type of state attribute
        """
        self.assertEqual(type(State.name), str)

    def test_basic_attribute(self):
        """
        Test for the basic attribute
        """
        self.temp_b.name = "michael"
        self.temp_b.xyz = 400
        self.assertEqual(self.temp_b.name, "michael")
        self.assertEqual(self.temp_b.xyz, 400)

    def test_return_string(self):
        """
        Test for the string method
        """
        my_str = str(self.temp_b)
        id_test = "[{}] ({})".format(self.temp_b.__class__.__name__,
                                     self.temp_b.id)
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
        Test for the to_dict method/datetime format
        """
        my_dict = self.temp_b.to_dict()
        created_at = my_dict['created_at']
        time = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.temp_b.created_at, time)

    def test_from_dict(self):
        """
        Test the from_dict method
        """
        my_dict = self.temp_b.to_dict()
        my_base = self.temp_b.__class__(**my_dict)
        self.assertEqual(my_base.id, self.temp_b.id)
        self.assertEqual(my_base.updated_at, self.temp_b.updated_at)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)
        self.assertEqual(my_base.__class__.__name__,
                         self.temp_b.__class__.__name__)

    def test_from_dict_n(self):
        """
        Test for the from_dict method
        """
        self.temp_b.random = "hello!"
        self.temp_b.z = 55
        my_dict = self.temp_b.to_dict()
        self.assertEqual(my_dict['z'], 55)
        my_base = self.temp_b.__class__(**my_dict)
        self.assertEqual(my_base.z, self.temp_b.z)
        self.assertEqual(my_base.random, self.temp_b.random)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)

    def test_unique_id(self):
        """
        Test for unique ids for the
        class objects
        """
        another = self.temp_b.__class__()
        another2 = self.temp_b.__class__()
        self.assertNotEqual(self.temp_b.id, another.id)
        self.assertNotEqual(self.temp_b.id, another2.id)

    def test_id_type_string(self):
        """
        Test for type string/id
        """
        self.assertEqual(type(self.temp_b.id), str)

    def test_updated_time(self):
        """
        Time update test
        """
        time1 = self.temp_b.updated_at
        self.temp_b.save()
        time2 = self.temp_b.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime.datetime)
