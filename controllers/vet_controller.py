from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.src.vet import Vet

import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)

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