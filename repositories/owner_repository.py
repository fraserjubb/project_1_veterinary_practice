from db.run_sql import run_sql

from models.owner import Owner


# Create
def save(owner):
    sql = "INSERT INTO owners (name, phone_number) VALUES (%s, %s) RETURNING id" # createing a sql statement and saving it into a variable
    values = [owner.name, owner.contact_number] # substiuiting the place holders in our sql for hte values passed into to prevent SQL injection 
    results = run_sql( sql, values ) # NORT SURE will ask an insturctorb 
    owner.id = results [0]["id"]
    return owner


# Read
def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['phone_number'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        owner = Owner(result["name"], result["phone_number"], result["id"])
    return owner
    

# Update
def update_owner_details(owner):
    sql = "UPDATE owners SET (name, phone_number) = (%s, %s) WHERE id = %s"
    values = [owner.name, owner.phone_number, owner.id]
    run_sql(sql, values)

# Delete
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

