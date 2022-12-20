from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)


# Create
@pets_blueprint.route("/pets", methods=['POST'])
def create_pet():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type_of_animal = request.form['type_of_animal']
    medical_history = request.form['medical_history']
    owner  = owner_repository.select(request.form['owner_id'])
    vet  = vet_repository.select(request.form['vet_id'])
    new_pet = Pet(name, date_of_birth, type_of_animal, medical_history, owner, vet)
    pet_repository.save(new_pet)
    return redirect('/pets')


@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    owners = owner_repository.select_all() 
    vets = vet_repository.select_all()
    return render_template("/pets/new.html", owners = owners, vets= vets)


# Read > Show all pets
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all() 
    return render_template("/pets/index.html", pets = pets)

# Read > Show individual pet
@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    return render_template("/pets/show.html", pet=pet)


# Edit > Need a page to view to enable an update/edit.
@pets_blueprint.route("/pets/<id>/edit", methods = ['GET'])
def edit_pet_details(id):
    pet = pet_repository.select(id)
    return render_template("/pets/edit.html", pet = pet)

# Update
@pets_blueprint.route("/pets/<id>", methods = ['POST'])
def update_pet_details(id):
    pet = pet_repository.select(id)
    pet.name = request.form['name']
    pet.date_of_birth = request.form['date_of_birth']
    pet.type_of_animal = request.form['type_of_animal']
    pet.medical_history = request.form['medical_history']
    # pet.owner  = owner_repository.update_owner_details(request.form['owner_id'])
    # owner_repository.update_owner_details(Owner)
    pet_repository.update_pet_details(pet)
    return redirect(f'/pets/{id}')

@pets_blueprint.route("/pets/<id>", methods = ['POST'])
def add_treatment_notes(id):
    pet = pet_repository.select(id)
    pet.medical_history = request.form['medical_history']
    pet_repository.add_medical_notes(pet)
    return redirect(f'/pets/{id}')



# Delete
@pets_blueprint.route("/pets/<id>/delete", methods = ['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')