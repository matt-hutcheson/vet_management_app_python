DROP TABLE if exists treatments;
DROP TABLE if exists patients;
DROP TABLE if exists vets;
DROP TABLE if exists clients;


CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    job_title VARCHAR(255)
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(255),
    address TEXT,
    registered BOOLEAN,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    breed VARCHAR(255),
    gender BOOLEAN,
    status VARCHAR(255),
    check_in_date VARCHAR(255),
    check_out_date VARCHAR(255),
    client_id INT REFERENCES clients(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    notes TEXT,
    patient_id INT REFERENCES patients(id) ON DELETE CASCADE
);