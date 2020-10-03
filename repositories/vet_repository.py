from db.run_sql import run_sql

from models.src.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, job_title) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.job_title]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

