from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
# import repositories.location_repository as location_repository

pets_blueprint = Blueprint("pets", __name__)


# Create
@pets_blueprint.route("/pets/", methods=['POST'])
def create_pet():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type_of_animal = request.form['type_of_animal']
    new_pet = Pet(name, date_of_birth, type_of_animal)
    pet_repository.save(new_pet)
    return redirect('/pets')


@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    return render_template("pets/new.html", pets = pets)


# Read
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all() 
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    # locations = location_repository.locations_for_user(user)
    return render_template("pets/show.html", pet=pet)


# Update



# Delete
@pets_blueprint.route("/pets/<id>/delete", methods = ['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')