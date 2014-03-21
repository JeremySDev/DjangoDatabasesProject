Running `python manage.py sql PetDispense` attached to terminal... up, run.7507
[33mBEGIN;[0m
[33mCREATE TABLE[0m [1m"PetDispense_species"[0m (
    [32;1m"species_id"[0m [32minteger[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"species_name"[0m [32mvarchar(100)[0m [33mNOT NULL[0m
)
;
[33mCREATE TABLE[0m [1m"PetDispense_breeds"[0m (
    [32;1m"breed_id"[0m [32minteger[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"breed_name"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"species_id"[0m [32minteger[0m [33mNOT NULL[0m [33mREFERENCES[0m [1m"PetDispense_species"[0m ([32;1m"species_id"[0m) DEFERRABLE INITIALLY DEFERRED
)
;
[33mCREATE TABLE[0m [1m"PetDispense_animalinfo"[0m (
    [32;1m"animal_id"[0m [32minteger[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"animal_name"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"species_id"[0m [32minteger[0m [33mNOT NULL[0m [33mREFERENCES[0m [1m"PetDispense_species"[0m ([32;1m"species_id"[0m) DEFERRABLE INITIALLY DEFERRED,
    [32;1m"breed_id"[0m [32minteger[0m [33mNOT NULL[0m [33mREFERENCES[0m [1m"PetDispense_breeds"[0m ([32;1m"breed_id"[0m) DEFERRABLE INITIALLY DEFERRED,
    [32;1m"in_shelter"[0m [32mboolean[0m [33mNOT NULL[0m
)
;
[33mCREATE TABLE[0m [1m"PetDispense_owners"[0m (
    [32;1m"owner_id"[0m [32minteger[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"owner_lastname"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"owner_firstname"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"owner_phone"[0m [32minteger[0m [33mNOT NULL[0m,
    [32;1m"owner_address"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"animal_id"[0m [32minteger[0m [33mNOT NULL[0m [33mREFERENCES[0m [1m"PetDispense_animalinfo"[0m ([32;1m"animal_id"[0m) DEFERRABLE INITIALLY DEFERRED
)
;
[33mCREATE TABLE[0m [1m"PetDispense_medicalinfo"[0m (
    [32;1m"id"[0m [32mserial[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"animal_id"[0m [32minteger[0m [33mNOT NULL[0m [33mREFERENCES[0m [1m"PetDispense_animalinfo"[0m ([32;1m"animal_id"[0m) DEFERRABLE INITIALLY DEFERRED,
    [32;1m"vaccinations"[0m [32mvarchar(100)[0m [33mNOT NULL[0m,
    [32;1m"has_illness"[0m [32mboolean[0m [33mNOT NULL[0m,
    [32;1m"illness"[0m [32mvarchar(100)[0m [33mNOT NULL[0m
)
;

[33mCOMMIT;[0m
