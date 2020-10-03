DROP TABLE if exists vets;
DROP TABLE if exists clients;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    job_title VARCHAR(255)
)

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(255),
    address VARCHAR(MAX),
    registered BOOLEAN
)