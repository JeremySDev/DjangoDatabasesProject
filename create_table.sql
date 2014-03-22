BEGIN;
CREATE TABLE "PetDispense_species" (
    "species_id" integer NOT NULL PRIMARY KEY,
    "species_name" varchar(100) NOT NULL
)
;
CREATE TABLE "PetDispense_breeds" (
    "breed_id" integer NOT NULL PRIMARY KEY,
    "breed_name" varchar(100) NOT NULL,
    "species_id" integer NOT NULL REFERENCES "PetDispense_species" ("species_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "PetDispense_animalinfo" (
    "animal_id" integer NOT NULL PRIMARY KEY,
    "animal_name" varchar(100) NOT NULL,
    "species_id" integer NOT NULL REFERENCES "PetDispense_species" ("species_id") DEFERRABLE INITIALLY DEFERRED,
    "breed_id" integer NOT NULL REFERENCES "PetDispense_breeds" ("breed_id") DEFERRABLE INITIALLY DEFERRED,
    "birth_date" date NOT NULL,
    "in_shelter" boolean NOT NULL
)
;
CREATE TABLE "PetDispense_owners" (
    "owner_id" integer NOT NULL PRIMARY KEY,
    "owner_lastname" varchar(100) NOT NULL,
    "owner_firstname" varchar(100) NOT NULL,
    "owner_phone" integer NOT NULL,
    "owner_address" varchar(100) NOT NULL,
    "animal_id" integer NOT NULL REFERENCES "PetDispense_animalinfo" ("animal_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "PetDispense_medicalinfo" (
    "id" serial NOT NULL PRIMARY KEY,
    "animal_id" integer NOT NULL REFERENCES "PetDispense_animalinfo" ("animal_id") DEFERRABLE INITIALLY DEFERRED,
    "vaccinations" varchar(100) NOT NULL,
    "has_illness" boolean NOT NULL,
    "illness" varchar(100) NOT NULL
)
;

COMMIT;
