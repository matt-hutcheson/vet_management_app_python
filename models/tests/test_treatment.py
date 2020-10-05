import unittest

from models.src.treatment import Treatment
from models.src.client import Client
from models.src.patient import Patient
from models.src.vet import Vet

class TestTreatment(unittest.TestCase):
    def setUp(self):
        self.test_vet = Vet("Bob", "Wiseman", "Graduate")
        self.test_client = Client("Vic", "Simpson", "07777 777 777", "123 Sesame Street", True, self.test_vet)
        self.test_patient = Patient("Rex", "05/05/2019", "Dog", "Bulldog", "Male", "Alive", self.test_vet, self.test_client, "02/11/2020", "05/11/2020")
        self.test_treatment = Treatment("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "04/10/2020", self.test_patient, self.test_vet)

    def test_treatment_exists(self):
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", self.test_treatment.notes)
        self.assertEqual(None, self.test_treatment.id)
        self.assertEqual("Bob", self.test_treatment.vet.first_name)
        self.assertEqual("Rex", self.test_treatment.patient.name)