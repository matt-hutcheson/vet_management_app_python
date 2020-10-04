import pdb

from models.src.vet import Vet
from models.src.client import Client
from models.src.patient import Patient

import repositories.vet_repository as vet_repository
import repositories.client_repository as client_repository
import repositories.patient_repository as patient_repository

patient_repository.delete_all()
client_repository.delete_all()
vet_repository.delete_all()

# Vet Repo Tests
vet_1 = Vet("Lin", "McDonald", "Graduate Vet")
vet_2 = Vet("Sharon", "Perkins", "Practice Partner")
vet_repository.save(vet_1)
vet_repository.save(vet_2)
vet_list = vet_repository.select_all()
vet_1 = vet_repository.select(vet_list[0].id)
vet_2 = vet_repository.select(vet_list[1].id)
selected_vet = vet_repository.select(vet_list[0].id)
# vet_repository.delete(vet_list[1].id)
vet_1.first_name = "Mary"
vet_repository.update(vet_1)
vet_list = vet_repository.select_all()

# Client repo tests
client_1 = Client("James", "McBean", "07666 666 666", "Baberton Mains Row, Edinburgh, EH12 1LS", True, vet_1)
client_2 = Client("Daniel", "Jackson", "07888 888 888", "Duke Street, Glasgow, G5 2FH", False, vet_2)
client_repository.save(client_1)
client_repository.save(client_2)
client_list = client_repository.select_all()
client_1 = client_repository.select(client_list[0].id)
client_2 = client_repository.select(client_list[1].id)
selected_client = client_repository.select(vet_list[0].id)
# client_repository.delete(client_1.id)
client_1.first_name = "Jim"
client_repository.update(client_1)
client_list = client_repository.select_all()

# Patient repo tests
patient_1 = Patient("Rex", "12/09/2019", "Dog", "Bulldog", "M", "Alive", vet_1, client_1, "03/10/2020", "10/10/2020")
patient_2 = Patient("Felix", "21/04/2016", "Cat", "British Shorthair", "F", "Alive", vet_2, client_2, "04/10/2020", "09/10/2020")
patient_3 = Patient("Tiger", "01/08/2018", "Cat", "Bengal", "M", "Alive", vet_2, client_2, "02/10/2020", "11/10/2020")
patient_repository.save(patient_1)
patient_repository.save(patient_2)
patient_repository.save(patient_3)

pdb.set_trace()