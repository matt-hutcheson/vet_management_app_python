from flask import Flask, render_template, redirect, request

from flask import Blueprint

from models.src.treatment import Treatment
from models.src.patient import Patient
from models.src.vet import Vet

import repositories.treatment_repository as treatment_repository
import repositories.patient_repository as patient_repository
import repositories.vet_repository as vet_repository

treatments_blueprint = Blueprint("treatments", __name__)

# INDEX - per patient
@treatments_blueprint.route('/treatments/<patient_id>')
def treatments(patient_id):
    treatments = treatment_repository.select_all(patient_id)
    patient = patient_repository.select(patient_id)
    return render_template('/treatments/index.html', all_treatments=treatments, selected_patient=patient)

# NEW
@treatments_blueprint.route('/treatments/<patient_id>/new')
def new_treatment(patient_id):
    patient = patient_repository.select(patient_id)
    vets = vet_repository.select_all()
    return render_template('/treatments/new.html', selected_patient=patient, all_vets=vets)

# CREATE

# EDIT

# UPDATE

# DELETE