import django_tables2 as tables
from PetDispense.models import AnimalInfo

speciesData = [
    {"species_id": 00001, "species_name": "Dog"}
]
breedData = [
    {"breed_id": 00001, "breed_name": "Shiba Inu", "species": speciesData}
]

animalData = [
    {"animal_id": 00001, "animal_name": "fido", "species": speciesData, "breed": breedData, "in_shelter": "true"},
]


class AnimalInfoTable(tables.Table):
    animal_name = tables.Column(verbose_name="animal name")

    class Meta:
        model = AnimalInfo



table = AnimalInfoTable(animalData)