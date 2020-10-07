from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.src.client import Client
from models.src.vet import Vet
from models.src.patient import Patient

import repositories.client_repository as client_repository
import repositories.vet_repository as vet_repository
import repositories.patient_repository as patient_repository

clients_blueprint = Blueprint("clients", __name__)

# INDEX
@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    clients.sort(key=lambda x: x.first_name)
    return render_template('/clients/index.html', all_clients=clients)

@clients_blueprint.route("/clients/<client_id>/all-pets")
def all_pets_clients(client_id):
    patients = client_repository.select_pets(client_id)
    patients.sort(key=lambda x: x.name)
    client = client_repository.select(client_id)
    patient_list = client.first_name + " " + client.last_name + " Pets"
    return render_template('/patients/index.html', all_patients = patients, patient_list=patient_list)

#  NEW
@clients_blueprint.route("/clients/new")
def new_client():
    vets = vet_repository.select_all()
    return render_template('clients/new.html', all_vets = vets)

# CREATE
@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    phone_number = request.form['phone-number'].replace(" ", "")
    address = request.form['address']
    if request.form['registered'] == "N":
        registered = False
    elif request.form['registered'] == "Y":
        registered = True
    vet_id = request.form['vet-assigned']
    vet = vet_repository.select(vet_id)
    client = Client(first_name, last_name,phone_number, address, registered, vet)
    client_repository.save(client)
    return redirect('/clients')

# EDIT
@clients_blueprint.route("/clients/<id>/edit", methods=["GET"])
def edit_client(id):
    client = client_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('/clients/edit.html', client=client, all_vets=vets)

# UPDATE
@clients_blueprint.route("/clients/<id>", methods=["POST"])
def update_client(id):
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    phone_number = request.form['phone-number'].replace(" ", "")
    address = request.form['address']
    if request.form['registered'] == "N":
        registered = False
    elif request.form['registered'] == "Y":
        registered = True
    vet_id = request.form['vet-assigned']
    vet = vet_repository.select(vet_id)
    client = Client(first_name, last_name,phone_number, address, registered, vet, id)
    client_repository.update(client)
    return redirect('/clients')

# DELETE
@clients_blueprint.route("/clients/<id>/delete", methods=["POST"])
def delete_client(id):
    client_repository.delete(id)
    return redirect('/clients')