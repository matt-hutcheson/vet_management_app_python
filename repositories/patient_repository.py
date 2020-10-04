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

def delete_all():
    sql = "DELETE FROM patients"
    run_sql(sql)

def select_all():
    patients = []
    sql = "SELECT * FROM patients"
    results = run_sql(sql)
    if results is not None:
        for row in results:
            vet = vet_repository.select(row['vet_id'])
            client = client_repository.select(row['client_id'])
            patient = Patient(row['name'], row['dob'], row['type'], row['breed'], row['gender'], row['status'], vet, client, row['check_in_date'], row['check_out_date'], row['id'])
            patients.append(patient)
    return patients

def select(id):
    sql = "SELECT * FROM patients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        vet = vet_repository.select(result['vet_id'])
        client = client_repository.select(result['client_id'])
        patient = Patient(result['name'], result['dob'], result['type'], result['breed'], result['gender'], result['status'], vet, client, result['check_in_date'], result['check_out_date'], result['id'])
    return patient

def delete(id):
    sql = "DELETE FROM patients WHERE id = %s"
    values = [id]
    run_sql(sql, values)

