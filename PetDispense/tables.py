import django_tables2 as tables
from PetDispense.models import Species, Breeds, AnimalInfo, Owners


class SpeciesTable(tables.Table):
    species_id = tables.Column(verbose_name="ID")
    species_name = tables.Column(verbose_name="species name")

    class Meta:
        model = Species


class BreedsTable(tables.Table):
    breed_id = tables.Column(verbose_name="ID")
    breed_name = tables.Column(verbose_name="breed name")
    species_name = tables.Column(verbose_name="species name")

    class Meta:
        model = Breeds
        sequence = ("breed_id", "breed_name", "species_name")
        exclude = ("species_id", "species")


class AnimalInfoTable(tables.Table):
    animal_name = tables.Column(verbose_name="animal name")
    species_name = tables.Column(verbose_name="species name")
    breed_name = tables.Column(verbose_name="breed name")

    class Meta:
        model = AnimalInfo
        sequence = ("animal_id", "animal_name", "species_name", "breed_name", "birth_date", "in_shelter")
        exclude = ("species", "breed")


class OwnersTable(tables.Table):
    animal_name = tables.Column(verbose_name="animal name")
    species_name = tables.Column(verbose_name="species name")
    breed_name = tables.Column(verbose_name="breed name")

    class Meta:
        model = Owners
        sequence = ("animal_name", "species_name", "breed_name", "owner_firstname", "owner_lastname")
        exclude = ("species", "breed")
