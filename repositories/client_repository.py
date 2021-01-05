from db.run_sql import run_sql

from models.src.client import Client
from models.src.vet import Vet
from models.src.patient import Patient

import repositories.vet_repository as vet_repository

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, phone_number, address, registered, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.phone_number, client.address, client.registered, client.vet.id]
    results = run_sql(sql, values)
    if results is not None:
        client.id = results[0]['id']
        client.vet = vet_repository.select(results[0]['vet_id'])
    return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    if results is not None:
        for row in results:
            vet = vet_repository.select(row['vet_id'])
            client = Client(row['first_name'],row['last_name'], row['phone_number'], row['address'], row['registered'], vet, row['id'])
            clients.append(client)
    return clients

def select(id):
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        vet = vet_repository.select(result['vet_id'])
        client = Client(result['first_name'], result['last_name'], result['phone_number'], result['address'], result['registered'], vet, result['id'])
    return client

def select_pets(client_id):
    pets = []
    sql = "SELECT * FROM patients WHERE client_id = %s"
    values = [client_id]
    results = run_sql(sql, values)
    if results is not None:
        for row in results:
            vet = vet_repository.select(row['vet_id'])
            client = select(row['client_id'])
            pet = Patient(row['name'], row['dob'], row['type'], row['breed'], row['gender'], row['status'], vet, client, row['check_in_date'], row['check_out_date'], row['id'])
            pets.append(pet)
    return pets

def delete(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(client):
    sql = "UPDATE clients SET (first_name, last_name, phone_number, address, registered, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [client.first_name, client.last_name, client.phone_number, client.address, client.registered, client.vet.id, client.id]
    run_sql(sql, values)

# Select pets of client(id)
