-- DROP TABLE vets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS pets;


CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type_of_animal VARCHAR(255) NOT NULL,
    owner_id INT REFERENCES owners(id)
);

SELECT * FROM pets;


SELECT * FROM owners;


-- CREATE TABLE vets (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     pet_patient_id INT REFERENCES pets(id)
-- );

-- INSERT INTO pets (name, date_of_birth, type_of_animal) VALUES ('Daisy', '18/03/2015', 'Dog');
-- INSERT INTO pets (name, date_of_birth, type_of_animal) VALUES ('Garfield', '01/10/2008', 'Cat');
-- INSERT INTO pets (name, date_of_birth, type_of_animal) VALUES ('Cerberus', '06/06/2006', 'Dog');
-- INSERT INTO pets (name, date_of_birth, type_of_animal) VALUES ('Luna', '20/11/2001', 'Cat');
-- INSERT INTO pets (name, date_of_birth, type_of_animal) VALUES ('Smudge', '29/12/2019', 'Rabbit');

-- SELECT * FROM pets;

-- INSERT INTO customers (name, phone_number, pet_id) VALUES ('Fraser Jubb', '07932773255', 1);
-- INSERT INTO customers (name, phone_number, pet_id) VALUES ('Satan', '66666666666', 3);
-- INSERT INTO customers (name, phone_number, pet_id) VALUES ('Jon Arbuckle', '01234567890', 2);

-- SELECT * FROM customers;

-- INSERT INTO vets (name, pet_patient_id) VALUES ('Dr R. Williams', 1);
-- INSERT INTO vets (name, pet_patient_id) VALUES ('Dr S. Clause', 3);

-- SELECT * FROM vets;

-- -- - name - string
-- -- - date_of_birth - string
-- -- - species - string
-- -- - breed - string
-- -- - ID
-- -- - medical_history - empty list