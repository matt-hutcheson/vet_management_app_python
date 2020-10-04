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
    return render_template('/clients/index.html', all_clients=clients)

#  NEW
@clients_blueprint.route("clients/new")
def new_client():
    return render_template('clients/new.html')

# CREATE
@clients_blueprint.route("clients", methods=["POST"])
def create_client():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    phone_number = request.form['phone-number']
    address = request.form['address']
    registered = request.form['registered']
    vet_id = request.form['vet-id']
    vet = vet_repository.select(vet_id)
    client = Client(first_name, last_name,phone_number, address, registered, vet)
    client_repository.save(client)
    return redirect('/clients')

# EDIT

# UPDATE