from flask import Flask, render_template, redirect, request, url_for

from flask import Blueprint

from models.src.treatment import Treatment
from models.src.patient import Patient
from models.src.vet import Vet
from models.src.date_changer import *

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
    date = date_today()
    return render_template('/treatments/new.html', selected_patient=patient, all_vets=vets, date_today=date)

@treatments_blueprint.route('/treatments/new')
def new_treatment_select_patient():
    patients = patient_repository.select_all()
    return render_template('/treatments/select_patient.html', all_patients=patients)

@treatments_blueprint.route('/treatments/select-patient', methods=["POST"])
def new_patient():
    selected_patient = patient_repository.select(request.form["patient-name"])
    patients = patient_repository.select_all()
    vets = vet_repository.select_all()
    date = date_today()
    print(date)
    return render_template('treatments/new.html', selected_patient=selected_patient, all_patients=patients, all_vets=vets, date_today=date)

# CREATE
@treatments_blueprint.route('/treatments/<patient_id>/create', methods=['POST'])
def create_treatment(patient_id):
    patient_id = patient_id
    print(patient_id)
    vet_id = request.form['vet-name']
    date = date_box_to_date(request.form['date'])
    notes = request.form['notes']
    patient = patient_repository.select(patient_id)
    vet = vet_repository.select(vet_id)
    treatment = Treatment(notes, date, patient, vet)
    treatment_repository.save(treatment)
    return redirect(url_for('.treatments', patient_id=patient_id))

# EDIT
@treatments_blueprint.route('/treatments/<patient_id>/<treatment_id>/edit', methods=['GET'])
def edit_treatment(patient_id, treatment_id):
    treatment = treatment_repository.select(treatment_id)
    vets = vet_repository.select_all()
    date = date_to_date_box(treatment.date)
    return render_template('/treatments/edit.html', treatment=treatment, all_vets=vets, date=date)

# UPDATE
@treatments_blueprint.route('/treatments/<patient_id>/<treatment_id>', methods=['POST'])
def update_treatment(patient_id, treatment_id):
    patient = patient_repository.select(patient_id)
    vet_id = request.form['vet-name']
    vet = vet_repository.select(vet_id)
    date = date_box_to_date(request.form['date'])
    notes = request.form['notes']
    treatment = Treatment(notes, date, patient, vet, treatment_id)
    treatment_repository.update(treatment)
    return redirect(url_for('.treatments', patient_id=patient_id))

# DELETE
@treatments_blueprint.route('/treatments/<patient_id>/<treatment_id>/delete', methods=['POST'])
def delete_treatment(patient_id, treatment_id):
    treatment_repository.delete(treatment_id)
    return redirect(url_for('.treatments', patient_id=patient_id))