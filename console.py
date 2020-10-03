import pdb

from models.src.vet import Vet

import repositories.vet_repository as vet_repository

vet_1 = Vet("Lin", "McDonald", "Graduate Vet")
vet_2 = Vet("Sharon", "Perkins", "Practice Partner")

vet_repository.save(vet_1)
vet_repository.save(vet_2)

pdb.set_trace()