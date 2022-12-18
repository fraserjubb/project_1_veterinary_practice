from db.run_sql import run_sql

from models.pet import Pet

def save(pet):
    sql = "INSERT INTO pets( name, date_of_birth, type_of_animal ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [pet.name, pet.date_of_birth, pet.type_of_animal]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], row['id'])
        pets.append(pet)
    return pets


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)


def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if len(results) > 0:
        if results:
            result = results[0]
            pet = Pet(result['name'], result['date_of_birth'], result['type_of_animal'], result['id'] )
        return pet

# Not currently doing anything
# def update(pet):
#     sql = "INSERT pets SET (name, date_of_birth, type_of_animal) = (%s, %s, %s) WHERE id = %s"
#     values = [pet.name, pet.date_of_birth, pet.type_of_animal, pet.id]
#     print(values)
#     run_sql(sql, values)

def delete(id):
    sql = "DELETE pets WHERE id= %s"
    values = [id]
    run_sql(sql, values)