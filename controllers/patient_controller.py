from flask import Flask, render_template, redirect, request
from flask import Blueprint
import datetime

from models.src.client import Client
from models.src.vet import Vet
from models.src.patient import Patient
from models.src.date_changer import *
from models.src.pet_lists import *

import repositories.patient_repository as patient_repository
import repositories.client_repository as client_repository
import repositories.vet_repository as vet_repository

patients_blueprint = Blueprint("patients", __name__)

# INDEX
@patients_blueprint.route('/patients')
def patients():
    patients = patient_repository.select_all()
    patients.sort(key=lambda x: x.name)
    patient_list = "All Patients"
    return render_template('patients/index.html', all_patients = patients, patient_list = patient_list)

@patients_blueprint.route('/patients/checked-in')
def checked_in_patients():
    patients = patient_repository.select_all()
    patients.sort(key=lambda x: x.name)
    patient_list = "In Patients"
    for patient in patients:
        if patient.checked_in == False:
            patients.remove(patient)
    return render_template('patients/index.html', all_patients=patients, patient_list=patient_list)

# NEW
@patients_blueprint.route('/patients/new', methods=["GET"])
def new_patient_get_client():
    clients = client_repository.select_all()
    date = date_today()
    return render_template('patients/select_client.html', all_clients=clients, date_today=date)

@patients_blueprint.route('/patients/select-client', methods=["POST"])
def new_patient():
    selected_client = client_repository.select(request.form["client-name"])
    selected_vet = vet_repository.select(selected_client.vet.id)
    clients = client_repository.select_all()
    vets = vet_repository.select_all()
    pet_types.sort()
    date = date_today()
    return render_template('patients/new.html', selected_client=selected_client, selected_vet=selected_vet, all_clients=clients, all_vets=vets, pet_types=pet_types, date_today=date)

# CREATE
@patients_blueprint.route('/patients/create', methods=["POST"])
def create_patient():
    name = request.form['name']
    type = request.form['type']
    breed = request.form['breed']
    client_id = request.form['client-name']
    client = client_repository.select(client_id)
    vet_id = request.form['vet-name']
    vet = vet_repository.select(vet_id)
    if request.form['dob-select'] == "date":
        dob = date_box_to_date(request.form['dob'])
    elif request.form['dob-select'] == "age":
        dob = date_box_to_date(age_to_date(request.form['age']))
    if request.form['gender'] == "Male":
        gender = "M"
    elif request.form['gender'] == "Female":
        gender = "F"
    status = request.form['status']
    check_in = date_box_to_date(request.form['check-in']) 
    check_out = date_box_to_date(request.form['check-out']) 
    patient = Patient(name, dob, type, breed, gender, status, vet, client, check_in, check_out)
    patient_repository.save(patient)
    return redirect('/patients')

# EDIT
@patients_blueprint.route('/patients/<id>/edit', methods=["GET"])
def edit_patient(id):
    patient = patient_repository.select(id)
    clients = client_repository.select_all()
    vets = vet_repository.select_all()
    dob = date_to_date_box(patient.dob)
    check_in = date_to_date_box(patient.check_in_date)
    check_out = date_to_date_box(patient.check_out_date)
    pet_types.sort()
    return render_template('/patients/edit.html', patient=patient, all_clients=clients, all_vets=vets, dob=dob, check_in=check_in, check_out=check_out, pet_types=pet_types)

# UPDATE
@patients_blueprint.route('/patients/<id>', methods=["POST"])
def update_patient(id):
    name = request.form['name']
    type = request.form['type']
    breed = request.form['breed']
    client_id = request.form['client-name']
    client = client_repository.select(client_id)
    vet_id = request.form['vet-name']
    vet = vet_repository.select(vet_id)
    dob = date_box_to_date(request.form['dob'])
    if request.form['gender'] == "Male":
        gender = "M"
    elif request.form['gender'] == "Female":
        gender = "F"
    status = request.form['status']
    check_in = date_box_to_date(request.form['check-in'])
    check_out = date_box_to_date(request.form['check-out'])
    patient = Patient(name, dob, type, breed, gender, status, vet, client, check_in, check_out, id)
    patient_repository.update(patient)
    return redirect('/patients')

# DELETE
@patients_blueprint.route('/patients/<id>/delete', methods=["POST"])
def delete_patient(id):
    patient_repository.delete(id)
    return redirect('/patients')