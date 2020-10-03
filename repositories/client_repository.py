from db.run_sql import run_sql

from models.src.client import Client

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, phone_number, address, registered) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.phone_number, client.address, client.registered]
    results = run_sql(sql, values)
    client.id = results[0]['id']
    return client

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for row in results:
        client = Client(row['first_name'],row['last_name'], row['phone_number'], row['address'], row['registered'], row['id'])
        clients.append(client)
    return clients

    