--get all the owners firstname and their animals name
SELECT
  "PetDispense_animalinfo".animal_id,
  animal_name,
  owner_firstname
FROM "PetDispense_animalinfo"
  NATURAL JOIN "PetDispense_owners";

--gets all the pets that have medicine info with there names as well
SELECT
  "PetDispense_animalinfo".animal_id,
  animal_name,
  vaccinations,
  has_illness,
  illness
FROM "PetDispense_animalinfo"
  NATURAL JOIN "PetDispense_medicalinfo";

--gets the names of the animal, its species, and its breed
SELECT
  "PetDispense_animalinfo".animal_id,
  animal_name,
  species_name,
  breed_name
FROM "PetDispense_animalinfo"
  NATURAL JOIN ("PetDispense_breeds"
    NATURAL JOIN "PetDispense_species");

--shows the animals name, its breed, and whether or not its in the shelter
SELECT
  "PetDispense_animalinfo".animal_id,
  in_shelter
FROM "PetDispense_animalinfo"
  NATURAL JOIN "PetDispense_breeds";

--shows the animals name, whether or not its in the shelter, and if it is ill
SELECT
  "PetDispense_animalinfo".animal_id,
  animal_name,
  in_shelter,
  has_illness
FROM "PetDispense_animalinfo"
  NATURAL JOIN "PetDispense_medicalinfo";

--finds all animal born before 1995
SELECT
  animal_name,
  breed_name,
  species_name,
  birth_date
FROM "PetDispense_animalinfo"
  NATURAL JOIN ("PetDispense_breeds"
    NATURAL JOIN "PetDispense_species")
GROUP BY animal_name, breed_name, species_name, birth_date
HAVING birth_date < '1995-01-01';

--find the youngest animal in the shelter
SELECT
  animal_name,
  birth_date,
  in_shelter
FROM "PetDispense_animalinfo"
  JOIN (SELECT
          max(birth_date) AS max_age
        FROM "PetDispense_animalinfo"
        WHERE in_shelter = 'true') AS "t1" ON t1.max_age = "PetDispense_animalinfo".birth_date;

--sorts by youngest
SELECT
  *
FROM "PetDispense_animalinfo"
ORDER BY birth_date ASC;

--finds all cats and dogs
(SELECT
   animal_id,
   animal_name,
   species_name
 FROM "PetDispense_animalinfo"
   NATURAL JOIN "PetDispense_species"
 WHERE species_name = 'Cat')
UNION
(SELECT
   animal_id,
   animal_name,
   species_name
 FROM "PetDispense_animalinfo"
   NATURAL JOIN "PetDispense_species"
 WHERE species_name = 'Dog');

--how many animal are in the shelter
SELECT
  count(*)
FROM "PetDispense_animalinfo"
WHERE in_shelter = 'true';
