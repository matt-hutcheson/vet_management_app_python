import unittest

from models.src.treatment import Treatment

class TestTreatment(unittest.TestCase):
    def setUp(self):
        test_treatment = Treatment("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", None, None)

    def test_treatment_exists(self):
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", self.test_treatment.notes)
        self.assertEqual(None, self.test_treatment.client_id)
        self.assertEqual(None, self.test_treatment.id)