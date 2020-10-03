import pdb

from models.src.vet import Vet

import repositories.vet_repository as vet_repository

vet_repository.delete_all()

vet_1 = Vet("Lin", "McDonald", "Graduate Vet")
vet_2 = Vet("Sharon", "Perkins", "Practice Partner")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

vet_list = vet_repository.select_all()

selected_vet = vet_repository.select(vet_list[0].id)

vet_repository.delete(vet_list[1].id)

vet_list = vet_repository.select_all()

pdb.set_trace()