from django.db import models
import datetime
#import dateutil


class Species(models.Model):
    species_id = models.IntegerField(primary_key=True)
    species_name = models.CharField(max_length=100, blank=False, null=False)


class Breeds(models.Model):
    breed_id = models.IntegerField(primary_key=True)
    breed_name = models.CharField(max_length=100, blank=False, null=False)
    species = models.ForeignKey(Species)
    #species_name = species.species_name
    #characteristics


class AnimalInfo(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_name = models.CharField(max_length=100, blank=False, null=False)
    species = models.ForeignKey(Species)
    breed = models.ForeignKey(Breeds)
    #birth_date = models.DateField('birth date')
    in_shelter = models.BooleanField(default=True, blank=False, null=False)

    #@property
    #def age(self):
    #    TODAY = datetime.date.today()
    #    return u'%s' % dateutil.relativedelta(TODAY, self.birth_date).years

    @property
    def __unicode__(self):
        return self.animal_id  #, self.animal_name, self.species, self.breed, self.in_shelter


class Owners(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_lastname = models.CharField(max_length=100, blank=False, null=False)
    owner_firstname = models.CharField(max_length=100, blank=False, null=False)
    owner_phone = models.IntegerField(max_length=10, blank=False, null=False)
    owner_address = models.CharField(max_length=100, blank=False, null=False)
    animal = models.ForeignKey(AnimalInfo)


class MedicalInfo(models.Model):
    animal = models.ForeignKey(AnimalInfo)
    vaccinations = models.CharField(max_length=100, blank=False, null=False)
    has_illness = models.BooleanField(default=False, blank=False, null=False)
    illness = models.CharField(max_length=100, blank=False, null=False)