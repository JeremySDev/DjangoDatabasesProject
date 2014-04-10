from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import ListView
from django_tables2 import RequestConfig
from PetDispense.models import AnimalInfo
from PetDispense.tables import AnimalInfoTable
from PetDispense.models import Breeds
from PetDispense.tables import BreedsTable
from PetDispense.models import Species
from PetDispense.tables import SpeciesTable
from PetDispense.forms import PostForm


def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content,
                                         created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))

    return render(request, 'PetDispense/query.html', {
        'form': form,
    })


def search(request):
    results = None
    query = request.GET.get('q')
    try:
        query = int(query)
    except ValueError:
        query = None
        results = None
    if query:
        results = AnimalInfo.objects.get(uid=query)
    context = RequestContext(request)
    return render_to_response('PetDispense/results.html', {"results": results}, context_instance=context)


def query(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("PetDispense/query.html", c)


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("PetDispense/index.html", c)


def selection(request):
    return render_to_response('PetDispense/selection.html')


def contact(request):
    return render_to_response('PetDispense/contact.html')


def about(request):
    return render_to_response('PetDispense/about.html')


def agreement(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("PetDispense/agreement.html", c)


def confirm(request):
    return render_to_response('PetDispense/confirm.html')


def returns(request):
    return render_to_response('PetDispense/returns.html')


def pin(request):
    return render_to_response('PetDispense/pin.html')


def animal(request):
    table = AnimalInfoTable(AnimalInfo.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/animals.html', {'table': table})


def breeds(request):
    table = BreedsTable(Breeds.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/breeds.html', {'table': table})


def species(request):
    table = SpeciesTable(Species.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/species.html', {'table': table})


class AnimalList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'not_in_shelter_list'

    def get_queryset(self):
        return AnimalInfo.objects.filter(in_shelter__exact='false')


class AgeList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'age_list'

    def get_queryset(self):
        return AnimalInfo.objects.order_by('-birth_date')


class OwnerList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'owner_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT "PetDispense_animalinfo".animal_id, animal_name, owner_firstname ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_owners"')


class MedInfoList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'medinfo_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT "PetDispense_animalinfo".animal_id, animal_name, vaccinations, has_illness, illness ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_medicalinfo"')


class BasicInfoList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'basicinfo_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT "PetDispense_animalinfo".animal_id, animal_name, species_name, breed_name ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN ("PetDispense_breeds" ' +
                                      'NATURAL JOIN "PetDispense_species")')


class BasicInfo2List(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'basicinfo2_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT "PetDispense_animalinfo".animal_id, in_shelter ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_breeds"')


class ShelterSickList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'sheltersickinfo_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT "PetDispense_animalinfo".animal_id, animal_name, in_shelter, has_illness ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_medicalinfo"')


class YoungestList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'youngest_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT animal_id, animal_name, birth_date, in_shelter ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'JOIN (SELECT max(birth_date) AS max_age ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'WHERE in_shelter = true) ' +
                                      'AS "t1" ' +
                                      'ON t1.max_age = "PetDispense_animalinfo".birth_date')


class AgeSortList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'agesortinfo_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT * ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'ORDER BY birth_date ASC')


class CatDogList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'catdog_list'

    def get_queryset(self):
        cat = 'Cat'
        dog = 'Dog'
        return AnimalInfo.objects.raw('SELECT animal_id, animal_name, species_name ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_species" ' +
                                      'WHERE species_name = %s ' +
                                      'UNION ' +
                                      'SELECT animal_id, animal_name, species_name ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'NATURAL JOIN "PetDispense_species" ' +
                                      'WHERE species_name = %s', [cat], [dog])

#need new query can't really use this one because doesn't return rows


class CountInShelterList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'count_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT count(*) ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'WHERE in_shelter = true')






