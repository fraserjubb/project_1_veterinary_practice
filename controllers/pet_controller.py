from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
# import repositories.location_repository as location_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all() 
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    # locations = location_repository.locations_for_user(user)
    return render_template("pets/show.html", pet=pet) #locations=locations)

# @pets_blueprint.route("/pets/<id>", methods=['GET'])
# def show_pet(id):
#     pet = pet.select(id)
#     return render_template('pets/show.html', pet = pet)