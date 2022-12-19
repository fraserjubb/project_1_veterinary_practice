from models.pet import Pet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
owner_repository.delete_all()

# owners:
owner_1 = Owner('Fraser', '07932773255')
owner_repository.save(owner_1)

#pets:
pet_1 = Pet('Daisy', '01.01.2011', 'Dog', owner_1)
pet_repository.save(pet_1)

pet_2 = Pet('Garfield', '03.11.2005', 'Cat', owner_1)
pet_repository.save(pet_2)
 
pet_3 = Pet('Cerberus', '06.06.2006', 'Dog', owner_1)
pet_repository.save(pet_3)

pet_4 = Pet('WHY', '06.06.2006', 'Dog', owner_1)
pet_repository.save(pet_4)

