import unittest

from models.src.date_changer import *

class TestDateChanger(unittest.TestCase):
    def test_date_box_to_date(self):
        self.assertEqual("01/08/2020", date_box_to_date("2020-08-01"))

    def test_date_to_date_box(self):
        self.assertEqual("2020-08-01", date_to_date_box("01/08/2020"))

    def test_date_to_age(self):
        self.assertEqual(3, date_to_age("19/08/2017"))

    def test_age_to_date(self):
        self.assertEqual("2017-10-06", age_to_date(3))