import unittest

from models.src.patient import Patient

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.test_patient = Patient("Rex", "05/05/2019", "Dog", "Bulldog", "Male", "Alive", "02/11/2020", "05/11/2020")

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
        self.assertEqual(None, self.test_patient.client_id)
        self.assertEqual(None, self.test_patient.vet_id)

    @unittest.skip("Delete this line to run the test")
    def test_age_to_date(self):
        pass

    @unittest.skip("Delete this line to run the test")
    def test_date_to_age(self):
        pass