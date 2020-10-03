from db.run_sql import run_sql

from models.src.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, job_title) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.job_title]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row["first_name"], row["last_name"], row["job_title"], row["id"])
        vets.append(vet)
    return vets