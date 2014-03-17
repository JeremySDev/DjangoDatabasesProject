from PetDispense.models import AnimalInfo, Species, Breeds

s = Species(species_id=00001, species_name="Dog")
b = Breeds(breed_id=00001, breed_name="Shiba Inu", species=s)
a = AnimalInfo(animal_id=00001, animal_name="fido", species=s, breed=b, in_shelter="true")

s.save()
b.save()
a.save()