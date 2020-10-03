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
    vets = []
    pets = []
    clients = client_repository.select_all()
    for client in clients:
        vet = vet_repository.select(client.vet_id)
        vets.append(vet)
        # add code for patients of client once written
    return render_template('/clients/index.html', all_clients=clients, vets=vets, pets=pets)