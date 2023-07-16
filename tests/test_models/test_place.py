#!/usr/bin/python3
"""
Unittest for place.py
"""

from models.base_model import BaseModel
from models.place import Place
import datetime
import unittest


class TestPlaceModel(unittest.TestCase):
    """
    Class TestPlaceModel definition
    """
    def setUp(self):
        self.temp_b = Place()

    def tearDown(self):
        self.temp_b = None

    def test_type(self):
        """
        Main method for (type) testing of the place model
        """
        self.assertIsInstance(self.temp_b, Place)
        self.assertEqual(type(self.temp_b), Place)
        self.assertEqual(issubclass(self.temp_b.__class__, BaseModel), True)
        self.assertEqual(isinstance(self.temp_b, BaseModel), True)

    def test_city_id_type(self):
        """
        Test for the city ID type
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id_type(self):
        """
        Test for the user ID type
        """
        self.assertEqual(type(Place.user_id), str)

    def test_name_type(self):
        """
        Test for the name type
        """
        self.assertEqual(type(Place.name), str)

    def test_description_type(self):
        """
        Test for the description type
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms_p(self):
        """
        Test for the number of rooms
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms_p(self):
        """
        Test for the number of bathrooms
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest_p(self):
        """
        Test for the max guest method
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night_p(self):
        """
        Test for the price by night method
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        """
        Test for the place latitude
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """
        Test for the place longitude
        """
        self.assertEqual(type(Place.longitude), float)

    def test_basic_attribute(self):
        """
        Test for basic attribute
        """
        self.temp_b.name = "michael"
        self.temp_b.xyz = 400
        self.assertEqual(self.temp_b.name, "michael")
        self.assertEqual(self.temp_b.xyz, 400)

    def test_return_string(self):
        """
        Test for checking the string return value
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
        Test for to_dict method
        """
        my_dict = self.temp_b.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.temp_b.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.temp_b.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.temp_b.__class__.__name__)
        self.assertEqual(my_dict['id'], self.temp_b.id)

    def test_to_dict_more(self):
        """
        Test for to_dict method
        """
        my_dict = self.temp_b.to_dict()
        created_at = my_dict['created_at']
        time = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.temp_b.created_at, time)

    def test_from_dict(self):
        """
        Test for the from_dict method
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
        self.temp_b.random = "tests!"
        self.temp_b.z = 55
        self.temp_b.amenity_ids = ['90870987907', '0897909', '987907']
        my_dict = self.temp_b.to_dict()
        self.assertEqual(my_dict['z'], 55)
        my_base = self.temp_b.__class__(**my_dict)
        self.assertEqual(my_base.z, self.temp_b.z)
        self.assertEqual(my_base.random, self.temp_b.random)
        self.assertEqual(my_base.created_at, self.temp_b.created_at)
        self.assertEqual(type(my_base.number_rooms), int)
        self.assertEqual(type(my_base.number_bathrooms), int)
        self.assertEqual(type(my_base.max_guest), int)
        self.assertEqual(type(my_base.price_by_night), int)
        self.assertEqual(type(my_base.latitude), float)
        self.assertEqual(type(my_base.longitude), float)
        self.assertEqual(type(my_base.amenity_ids), list)
        self.assertEqual(self.temp_b.number_rooms, my_base.number_rooms)
        self.assertEqual(self.temp_b.number_bathrooms,
                         my_base.number_bathrooms)
        self.assertEqual(self.temp_b.max_guest, my_base.max_guest)
        self.assertEqual(self.temp_b.price_by_night, my_base.price_by_night)
        self.assertEqual(self.temp_b.latitude, my_base.latitude)
        self.assertEqual(self.temp_b.longitude, my_base.longitude)
        self.assertEqual(self.temp_b.amenity_ids, my_base.amenity_ids)

    def test_unique_id(self):
        """
        Test for unique IDs
        """
        another = self.temp_b.__class__()
        another2 = self.temp_b.__class__()
        self.assertNotEqual(self.temp_b.id, another.id)
        self.assertNotEqual(self.temp_b.id, another2.id)

    def test_id_type_string(self):
        """
        Test for ID type
        """
        self.assertEqual(type(self.temp_b.id), str)

    def test_updated_time(self):
        """
        Test time update
        """
        time1 = self.temp_b.updated_at
        self.temp_b.save()
        time2 = self.temp_b.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime.datetime)
