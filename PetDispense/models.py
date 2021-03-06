from django.db import models
from dateutil.relativedelta import relativedelta
import datetime
import dateutil


class Species(models.Model):
    species_id = models.IntegerField(primary_key=True)
    species_name = models.CharField(max_length=100, blank=False, null=False)


class Breeds(models.Model):
    breed_id = models.IntegerField(primary_key=True)
    breed_name = models.CharField(max_length=100, blank=False, null=False)
    species = models.ForeignKey(Species)

    @property
    def species_name(self):
        return u"%s" % self.species.species_name
        #characteristics


class AnimalInfo(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_name = models.CharField(max_length=100, blank=False, null=False)
    species = models.ForeignKey(Species)
    breed = models.ForeignKey(Breeds)
    birth_date = models.DateField('birth date')
    in_shelter = models.BooleanField(default=True, blank=False, null=False)

    @property
    def age(self):
        today = datetime.date.today()
        return u'%s' % (today.year - self.birth_date.year)

    @property
    def species_name(self):
        return u"%s" % self.species.species_name

    @property
    def breed_name(self):
        return u"%s" % self.breed.breed_name

    @property
    def __unicode__(self):
        return self.animal_id
        #, self.animal_name, self.species, self.breed, self.in_shelter


class Owners(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_lastname = models.CharField(max_length=100, blank=False, null=False)
    owner_firstname = models.CharField(max_length=100, blank=False, null=False)
    owner_phone = models.CharField(max_length=100, blank=False, null=False)
    owner_address = models.CharField(max_length=100, blank=False, null=False)
    animal = models.ForeignKey(AnimalInfo)


class MedicalInfo(models.Model):
    animal = models.ForeignKey(AnimalInfo)
    vaccinations = models.CharField(max_length=100, blank=False, null=False)
    has_illness = models.BooleanField(default=False, blank=False, null=False)
    illness = models.CharField(max_length=100, blank=False, null=False)