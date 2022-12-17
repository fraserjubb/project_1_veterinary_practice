from db.run_sql import run_sql

from models.pet import Pet
# from models.customer import Customer

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

# def select(id):
#     user = None
#     sql = "SELECT * FROM users WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
#     # Could alternativly have..
#     # if len(results) > 0 
#     if results:
#         result = results[0]
#         user = User(result['name'], result['id'] )
#     return user


# def users_for_location(location):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE location_id = %s"
#     values = [location.id]
#     results = run_sql(sql, values)

#     for row in results:
#         user = User(row['name'], row['id'])
#         users.append(user)

#     return users

# def user_for_visit(visit):
#     sql = "SELECT * FROM users WHERE id = %s"
#     values = [visit.user.id]
#     results = run_sql(sql, values)[0]
#     user = User(results['name'], results['id'])
#     return user


# def delete_all():
#     sql = "DELETE FROM users"
#     run_sql(sql)
