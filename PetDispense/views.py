from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import ListView
from django_tables2 import RequestConfig
from PetDispense.models import AnimalInfo, Owners
from PetDispense.tables import AnimalInfoTable
from PetDispense.models import Breeds
from PetDispense.tables import BreedsTable
from PetDispense.models import Species
from PetDispense.tables import SpeciesTable
from PetDispense.tables import OwnersTable
from PetDispense.forms import UserForm


############Search######################################################################################################
def query(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("PetDispense/query.html", c)


def search(request):
    global results
    query1 = request.GET.get('q')
    try:
        query2 = str(query1)
    except ValueError:
        query2 = None
        results = None
    if query2:
        results = AnimalInfo.objects.filter(animal_name=query2)
    context = RequestContext(request)
    return render_to_response('PetDispense/results.html', {"results": results}, context_instance=context)


def search_owners(request):
    global results_owner
    query1 = request.GET.get('qt')
    try:
        query2 = str(query1)
    except ValueError:
        query2 = None
        results_owner = None
    if query2:
        results_owner = Owners.objects.filter(owner_lastname=query2)
    context = RequestContext(request)
    return render_to_response('PetDispense/results2.html', {"results_owner": results_owner}, context_instance=context)


def dispense(request):
    an = request.GET.get('an')
    return render_to_response("PetDispense/petinfopage.html", {"an": an})


############Login#######################################################################################################
def index(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('agreement'))
        else:
            return HttpResponseRedirect(reverse('login_failure'))
    return render_to_response("PetDispense/index.html", c)


# Register a new user with a custom form, log them in, and redirect to the Warning page.
def new_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('agreement'))
    user_form = UserForm()
    return render(request, 'PetDispense/register.html', {'user_form': user_form})


def login_failure(request):
    return render_to_response('PetDispense/index_fail.html')


def logout_user(request):
    # logout the user
    logout(request)
    # go back to the login page
    return render(request, 'PetDispense/index.html')


###############Webpages#################################################################################################


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


def returns(request):
    return render_to_response('PetDispense/returns.html')


def confirm(request):
    return render_to_response('PetDispense/agreement.html')


###############List Views###############################################################################################
class AnimalList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'not_in_shelter_list'

    #return AnimalInfo.objects.filter(in_shelter='false')
    def get_queryset(self):
        return AnimalInfo.objects.raw(
            'SELECT "PetDispense_animalinfo".animal_id, animal_name ' +
            'FROM "PetDispense_animalinfo" ' +
            'WHERE in_shelter = false')


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
        return AnimalInfo.objects.raw(
            'SELECT "PetDispense_animalinfo".animal_id, animal_name, vaccinations, has_illness, illness ' +
            'FROM "PetDispense_animalinfo" ' +
            'NATURAL JOIN "PetDispense_medicalinfo"')


class BasicInfoList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'basicinfo_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw(
            'SELECT "PetDispense_animalinfo".animal_id, animal_name, species_name, breed_name ' +
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
        return AnimalInfo.objects.raw(
            'SELECT "PetDispense_animalinfo".animal_id, animal_name, in_shelter, has_illness ' +
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
                                      'WHERE species_name = %s', [cat])


class CountInShelterList(ListView):
    template_name = 'PetDispense/animalinfo_list.html'
    context_object_name = 'count_list'

    def get_queryset(self):
        return AnimalInfo.objects.raw('SELECT count(*) ' +
                                      'FROM "PetDispense_animalinfo" ' +
                                      'WHERE in_shelter = true')






