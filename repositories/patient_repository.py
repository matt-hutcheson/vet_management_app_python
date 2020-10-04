from db.run_sql import run_sql

from models.src.patient import Patient
import repositories.client_repository as client_repository
import repositories.vet_repository as vet_repository

def save(patient):
    sql = "INSERT INTO patients (name, dob, type, breed, gender, status, check_in_date, check_out_date, client_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [patient.name, patient.dob, patient.type, patient.breed, patient.gender, patient.status, patient.check_in_date, patient.check_out_date, patient.client.id, patient.vet.id]
    results = run_sql(sql,values)
    if results is not None:
        patient.id = results[0]['id']
        patient.client = client_repository.select(results[0]['client_id'])
        patient.vet = vet_repository.select(results[0]['vet_id'])
    return patient