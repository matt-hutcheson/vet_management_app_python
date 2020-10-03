import unittest

from models.src.vet import Vet

class TestVet(unittest.TestCase):
    def setUp(self):
        self.test_vet = Vet("John", "Smith", "Senior Vet")

    def test_vet_exists(self):
        self.assertEqual("John", self.test_vet.first_name)
        self.assertEqual("Smith", self.test_vet.last_name)
        self.assertEqual("Senior Vet", self.test_vet.job_title)
        self.assertEqual(None, self.test_vet.id)