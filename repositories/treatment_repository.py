from db.run_sql import run_sql

from models.src.treatment import Treatment

import repositories.patient_repository as patient_repository
import repositories.vet_repository as vet_repository

def save(treatment):
    sql = "INSERT INTO treatments (notes, date, patient_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [treatment.notes, treatment.date, treatment.patient.id, treatment.vet.id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        treatment.patient = patient_repository.select(result['patient_id'])
        treatment.vet = vet_repository.select(result['vet_id'])
        treatment.id = result['id']
    return treatment

def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def select_all(patient_id):
    treatments = []
    sql = "SELECT * FROM treatments WHERE patient_id = %s"
    values = [patient_id]
    results = run_sql(sql, values)
    if results is not None:
        for row in results:
            patient = patient_repository.select(row['patient_id'])
            vet = vet_repository.select(row['vet_id'])
            treatment = Treatment(row['notes'], row['date'], patient, vet, row['id'])
            treatments.append(treatment)
    return treatments

def select(id):
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        patient = patient_repository.select(result['patient_id'])
        vet = vet_repository.select(result['vet_id'])
        treatment = Treatment(result['notes'], result['date'], patient, vet, result['id'])
    return treatment

def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)