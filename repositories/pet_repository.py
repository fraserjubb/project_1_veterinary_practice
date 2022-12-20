from db.run_sql import run_sql

import repositories.owner_repository as owner_repo 
from models.pet import Pet


# Create
def save(pet):
    sql = "INSERT INTO pets( name, date_of_birth, type_of_animal, owner_id ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [pet.name, pet.date_of_birth, pet.type_of_animal, pet.owner.id]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


# Read > Show all pets
def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        owner = owner_repo.select(row['owner_id'])
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], owner, row['id'])
        pets.append(pet)
    return pets

# Read > Show individual pet
def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if len(results) > 0:
        result = results[0]
    for row in results:
        owner = owner_repo.select(row['owner_id'])
        pet = Pet(result['name'], result['date_of_birth'], result['type_of_animal'], owner, result['id'] )
    return pet


# Update
def update_pet_details(pet):
    sql = "UPDATE pets SET (name, date_of_birth, type_of_animal, owner) = (%s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.date_of_birth, pet.type_of_animal, pet.owner, pet.id]
    run_sql(sql, values)

# def assign_vet(pet):


# Delete
def delete(id):
    sql = "DELETE FROM pets WHERE id= %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)





