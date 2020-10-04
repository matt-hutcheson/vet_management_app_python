from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.src.client import Client
from models.src.vet import Vet
from models.src.patient import Patient

import repositories.patient_repository as patient_repository
import repositories.client_repository as client_repository
import repositories.vet_repository as vet_repository

patients_blueprint = Blueprint("patients", __name__)

# INDEX
@patients_blueprint.route('/patients')
def patients():
    patients = patient_repository.select_all()
    return render_template('patients/index.html', all_patients = patients)

# NEW
@patients_blueprint.route('/patients/new', methods=["GET"])
def new_patient_get_client():
    clients = client_repository.select_all()
    return render_template('patients/select_client.html', all_clients=clients)

@patients_blueprint.route('/patients/select-client', methods=["POST"])
def new_patient():
    selected_client = client_repository.select(request.form["client-name"])
    clients = client_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('patients/new.html', selected_client=selected_client, all_clients=clients, all_vets=vets)

# CREATE
@patients_blueprint.route('/patients', methods=["POST"])
def create_patient():
    name = request.form['name']
    type = request.form['type']
    breed = request.form['breed']
    client_id = request.form['client-name']
    client = client_repository.select(client_id)
    vet_id = request.form['vet-name']
    vet = vet_repository.select(vet_id)
    dob = request.form['dob']
    gender = request.form['gender']
    status = request.form['status']
    patient = Patient(name, dob, type, breed, gender, status, vet, client)
    patient_repository.save(patient)
    return redirect('/patients')

# EDIT

# UPDATE

# DELETE