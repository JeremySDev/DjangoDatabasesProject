import django_tables2 as tables
from PetDispense.models import Species, AnimalInfo


class SpeciesTable(tables.Table):
    species_id = tables.Column(verbose_name="ID")
    species_name = tables.Column(verbose_name="species name")

    class Meta:
        model = Species


class AnimalInfoTable(tables.Table):
    animal_name = tables.Column(verbose_name="animal name")
    species_name = tables.Column(verbose_name="species name")
    breed_name = tables.Column(verbose_name="breed name")
    class Meta:
        model = AnimalInfo
        sequence = ("animal_id", "animal_name", "species_name", "breed_name", "in_shelter")
        exclude = ("species", "breed")
