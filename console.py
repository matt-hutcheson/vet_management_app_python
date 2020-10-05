import pdb

from models.src.vet import Vet
from models.src.client import Client
from models.src.patient import Patient
from models.src.treatment import Treatment

import repositories.vet_repository as vet_repository
import repositories.client_repository as client_repository
import repositories.patient_repository as patient_repository
import repositories.treatment_repository as treatment_repository

treatment_repository.delete_all()
patient_repository.delete_all()
client_repository.delete_all()
vet_repository.delete_all()

# Vet Repo Tests
vet_1 = Vet("Lin", "McDonald", "Graduate Vet")
vet_2 = Vet("Sharon", "Perkins", "Practice Partner")
vet_1 = vet_repository.save(vet_1)
vet_2 = vet_repository.save(vet_2)
vet_list = vet_repository.select_all()
selected_vet = vet_repository.select(vet_list[0].id)
# vet_repository.delete(vet_list[1].id)
vet_1.first_name = "Mary"
vet_repository.update(vet_1)
vet_list = vet_repository.select_all()

# Client repo tests
client_1 = Client("James", "McBean", "07666666666", "1 Baberton Mains Row, Edinburgh, EH12 1LS", True, vet_1)
client_2 = Client("Daniel", "Jackson", "07888888888", "16 Duke Street, Glasgow, G5 2FH", False, vet_2)
client_1 = client_repository.save(client_1)
client_2 = client_repository.save(client_2)
client_list = client_repository.select_all()
selected_client = client_repository.select(vet_list[0].id)
# client_repository.delete(client_1.id)
client_1.first_name = "Jim"
client_repository.update(client_1)
client_list = client_repository.select_all()

# Patient repo tests
patient_1 = Patient("Rex", "12/09/2019", "Dog", "Bulldog", "M", "Alive", vet_1, client_1, "03/10/2020", "10/10/2020")
patient_2 = Patient("Felix", "21/04/2016", "Cat", "British Shorthair", "F", "Alive", vet_2, client_2, "04/10/2020", "09/10/2020")
patient_3 = Patient("Tiger", "01/08/2018", "Cat", "Bengal", "M", "Alive", vet_2, client_2, "02/10/2020", "11/10/2020")
patient_1 = patient_repository.save(patient_1)
patient_2 = patient_repository.save(patient_2)
patient_3 = patient_repository.save(patient_3)
patient_list = patient_repository.select_all()
selected_patient = patient_repository.select(patient_list[0].id)
# patient_repository.delete(patient_list[1].id)
patient_2.name = "Black Panther"
patient_repository.update(patient_2)
patient_list = patient_repository.select_all()

# Treatment repo tests
treatment_1 = Treatment("X-ray done on front left leg following car collision. Results sent to specialists at vet hospital. Awaiting results from specialist.", "02/10/2020", patient_1, vet_1)
treatment_2 = Treatment("Patient arrived with severe dehydration and heatstroke due to heatwave. Put in ice bath and on fluids and keeping overnight to monitor progress.", "03/10/2020", patient_2, vet_2)
treatment_3 = Treatment("Prepared patient for abdominable surgery following foreign object injestion.", "01/10/2020", patient_3, vet_1)
treatment_4 = Treatment("Patient underwent abdominal surgery and foreign object causing distress was successfully removed. Patient moved to intensive care for overnight observation", "02/10/2020", patient_3, vet_1)
treatment_1 = treatment_repository.save(treatment_1)
treatment_2 = treatment_repository.save(treatment_2)
treatment_3 = treatment_repository.save(treatment_3)
treatment_4 = treatment_repository.save(treatment_4)

treatment_list_patient_3 = treatment_repository.select_all(patient_3.id)
selected_treatment = treatment_repository.select(treatment_4.id)
# treatment_repository.delete(treatment_3.id)
treatment_list_patient_3 = treatment_repository.select_all(patient_3.id)
treatment_1.date = "30/09/2020"
treatment_repository.update(treatment_1)
selected_treatment = treatment_repository.select(treatment_1.id)

pdb.set_trace()