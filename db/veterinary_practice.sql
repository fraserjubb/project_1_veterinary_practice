DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;


CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255)
);


CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);



CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type_of_animal VARCHAR(255) NOT NULL,
    medical_history TEXT,
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id)
);