from models.pet import Pet
from models.owner import Owner
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

# owners:
owner_1 = Owner('Fraser Jubb', '07932773255')
owner_repository.save(owner_1)

owner_2 = Owner('Satan', '66666666666')
owner_repository.save(owner_2)

owner_3 = Owner('John Wick', '987460385024')
owner_repository.save(owner_3)

owner_4 = Owner('Master Splinter', '892782404818')
owner_repository.save(owner_4)


# vets:
vet_1 = Vet('Dr Do Little')
vet_repository.save(vet_1)

vet_2 = Vet('Dr R Williams')
vet_repository.save(vet_2)


#pets:
pet_1 = Pet('Daisy', '01.01.2017', 'Dog', '', owner_1, vet_2)
pet_repository.save(pet_1)

pet_2 = Pet('Garfield', '03.11.2005', 'Cat', 'Obesity issues likely due to excessive lasagne consumption.', owner_2, vet_1)
pet_repository.save(pet_2)
 
pet_3 = Pet('Cerberus', '06.06.2006', 'Dog', 'Has three heads and highly aggressive.', owner_2, vet_1)
pet_repository.save(pet_3)

pet_4 = Pet('Smudge', '06.12.2020', 'Rabbit','', owner_3, vet_1)
pet_repository.save(pet_4)

pet_5 = Pet('Leonardo', '06.12.2020', 'Turtle','', owner_4, vet_2)
pet_repository.save(pet_5)

pet_6 = Pet('Raphael', '06.12.2020', 'Turtle','', owner_4, vet_2)
pet_repository.save(pet_6)

pet_7 = Pet('Donatello', '06.12.2020', 'Turtle','', owner_4, vet_2)
pet_repository.save(pet_7)

pet_8 = Pet('Michelangelo', '06.12.2020', 'Turtle','', owner_4, vet_2)
pet_repository.save(pet_8)
