from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.src.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.patient_repository as patient_repository
import repositories.client_repository as client_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)

# INDEX PATIENTS OF VET
@vets_blueprint.route("/vets/<vet_id>/patients")
def vet_patients(vet_id):
    patients = vet_repository.select_patients(vet_id)
    vet = vet_repository.select(vet_id)
    return render_template("vets/index_patients.html", all_patients=patients, vet=vet)

# INDEX CLIENTS OF VET
@vets_blueprint.route("/vets/<vet_id>/clients")
def vet_clients(vet_id):
    clients = vet_repository.select_clients(vet_id)
    vet = vet_repository.select(vet_id)
    return render_template("vets/index_clients.html", all_clients=clients, vet=vet)

#  NEW
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

# CREATE
@vets_blueprint.route("/vets", methods=["POST"])
def create_vet():
    first_name = request.form["first-name"]
    print(first_name)
    last_name = request.form["last-name"]
    job_title = request.form["job-title"]
    new_vet = Vet(first_name, last_name, job_title)
    vet_repository.save(new_vet)
    return redirect("/vets")

# EDIT
@vets_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet=vet)

# UPDATE
@vets_blueprint.route("/vets/<id>", methods=["POST"])
def update_vet(id):
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    job_title = request.form["job-title"]
    id = request.form["id"]
    vet = Vet(first_name, last_name, job_title, id)
    vet_repository.update(vet)
    return redirect("/vets")

# DELETE
@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets")
