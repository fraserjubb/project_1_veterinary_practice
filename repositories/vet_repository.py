from db.run_sql import run_sql

from models.vet import Vet


# Create
def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING id" 
    values = [vet.name] 
    results = run_sql( sql, values )
    vet.id = results [0]["id"]
    return vet


# Read
def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        vet = Vet(result["name"], result["id"])
    return vet
    

# Update
def update_vet_details(vet):
    sql = "UPDATE vets SET (name) = (%s) WHERE id = %s"
    values = [vet.name, vet.id]
    run_sql(sql, values)

# Delete
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

