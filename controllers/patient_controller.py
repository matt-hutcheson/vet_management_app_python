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
@patients_blueprint.route('patients/new')
def new_patient():
    return render_template('patients/new.html')

# CREATE

# EDIT

# UPDATE

# DELETE