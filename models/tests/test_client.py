import unittest

from models.src.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.test_client = Client("Jack", "Sparrow", "07777 777 777", "123 Sesame Street, New York, NY12 4CD")

    def test_client_exists(self):
        self.assertEqual("Jack", self.test_client.first_name)
        self.assertEqual("Sparrow", self.test_client.last_name)
        self.assertEqual("07777 777 777", self.test_client.phone_number)
        self.assertEqual("123 Sesame Street, New York, NY12 4CD", self.test_client.address)
        self.assertEqual(False, self.test_client.registered)
        self.assertEqual(None, self.test_client.id)
