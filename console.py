import pdb
from models.pet import Pet

import repositories.pet_repository as pet_repository

pet_repository.delete_all()

pet_1 = Pet('Daisy', '01.01.2011', 'Doggy')
pet_repository.save(pet_1)

pet_2 = Pet('Garfield', '03.11.2005', 'Cat')
pet_repository.save(pet_2)

pet_3 = Pet('Cerberus', '06.06.2006', 'Doggy')
pet_repository.save(pet_3)

pdb.set_trace()