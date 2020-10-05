import unittest

from models.src.patient import Patient
from models.src.vet import Vet
from models.src.client import Client

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.test_vet = Vet("Bob", "Wiseman", "Graduate")
        self.test_client = Client("Vic", "Simpson", "07777 777 777", "123 Sesame Street", True, self.test_vet)
        self.test_patient = Patient("Rex", "05/05/2019", "Dog", "Bulldog", "Male", "Alive", self.test_vet, self.test_client, "02/11/2020", "05/11/2020")
        self.test_date = "2019-05-07"

    def test_patient_exists(self):
        self.assertEqual("Rex", self.test_patient.name)
        self.assertEqual("05/05/2019", self.test_patient.dob)
        self.assertEqual("Dog", self.test_patient.type)
        self.assertEqual("Bulldog", self.test_patient.breed)
        self.assertEqual("Male", self.test_patient.gender)
        self.assertEqual("Alive", self.test_patient.status)
        self.assertEqual("02/11/2020", self.test_patient.check_in_date)
        self.assertEqual("05/11/2020", self.test_patient.check_out_date)
        self.assertEqual(None, self.test_patient.id)
        self.assertEqual("Vic", self.test_patient.client.first_name)
        self.assertEqual("Bob", self.test_patient.vet.first_name)

    @unittest.skip("Delete this line to run the test")
    def test_age_to_date(self):
        pass

    @unittest.skip("Delete this line to run the test")
    def test_date_to_age(self):
        pass