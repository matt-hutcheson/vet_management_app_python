import pdb

from models.src.vet import Vet
from models.src.client import Client

import repositories.vet_repository as vet_repository
import repositories.client_repository as client_repository

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

pdb.set_trace()