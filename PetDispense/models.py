from django.db import models

# Create your models here.
class AnimalInfo(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_name = models.CharField(max_length=100, blank=False, null=False)
    species_name = models.ForeignKey(Species.species_name)
    breed_name = models.ForeignKey(Breeds.breed_name)
    age = models.IntegerField(max_length=3, blank=False, null=False)
    in_shelter = models.BooleanField(initial=True, blank=False, null=False)

class Owners(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_lastname = models.CharField(max_length=100, blank=False, null=False)
    owner_firstname = models.CharField(max_length=100, blank=False, null=False)
    owner_phone = models.IntegerField(max_length=10, blank=False, null=False)
    owner_address = models.CharField(max_length=100, blank=False, null=False)
    animal_id = models.ForeignKey(AnimalInfo.animal_id)

class MedicalInfo(models.Model):
     animal_id = models.ForeignKey(AnimalInfo.animal_id)
     animal_name = models.ForeignKey(AnimalInfo.animal_name)
     vaccinations = models.CharField(max_length=100, blank=False, null=False)
     has_illness = models.BooleanField(initial=False, blank=False, null=False)
     illness = models.CharField(max_length=100, blank=False, null=False)

class Breeds(models.Model):
    breed_id = models.IntegerField(primary_key=True)
    breed_name = models.CharField(max_length=100, blank=False, null=False)
    species_name = models.ForeignKey(Species.species_name)
    #characteristics

class Species(models.Model):
    species_id = models.IntegerField(primary_key=True)
    species_name = models.CharField(max_length=100, blank=False, null=False)
