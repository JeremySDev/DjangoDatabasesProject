BEGIN;
CREATE TABLE "PetDispense_species" (
  "species_id"   INTEGER      NOT NULL PRIMARY KEY,
  "species_name" VARCHAR(100) NOT NULL
);
CREATE TABLE "PetDispense_breeds" (
  "breed_id"   INTEGER      NOT NULL PRIMARY KEY,
  "breed_name" VARCHAR(100) NOT NULL,
  "species_id" INTEGER      NOT NULL REFERENCES "PetDispense_species" ("species_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "PetDispense_animalinfo" (
  "animal_id"   INTEGER      NOT NULL PRIMARY KEY,
  "animal_name" VARCHAR(100) NOT NULL,
  "species_id"  INTEGER      NOT NULL REFERENCES "PetDispense_species" ("species_id") DEFERRABLE INITIALLY DEFERRED,
  "breed_id"    INTEGER      NOT NULL REFERENCES "PetDispense_breeds" ("breed_id") DEFERRABLE INITIALLY DEFERRED,
  "birth_date"  DATE         NOT NULL,
  "in_shelter"  BOOLEAN      NOT NULL
);
CREATE TABLE "PetDispense_owners" (
  "owner_id"        INTEGER      NOT NULL PRIMARY KEY,
  "owner_lastname"  VARCHAR(100) NOT NULL,
  "owner_firstname" VARCHAR(100) NOT NULL,
  "owner_phone"     INTEGER      NOT NULL,
  "owner_address"   VARCHAR(100) NOT NULL,
  "animal_id"       INTEGER      NOT NULL REFERENCES "PetDispense_animalinfo" ("animal_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "PetDispense_medicalinfo" (
  "id"           SERIAL       NOT NULL PRIMARY KEY,
  "animal_id"    INTEGER      NOT NULL REFERENCES "PetDispense_animalinfo" ("animal_id") DEFERRABLE INITIALLY DEFERRED,
  "vaccinations" VARCHAR(100) NOT NULL,
  "has_illness"  BOOLEAN      NOT NULL,
  "illness"      VARCHAR(100) NOT NULL
);

COMMIT;
