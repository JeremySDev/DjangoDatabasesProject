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


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("PetDispense/index.html", c)


def selection(request):
    return render_to_response('PetDispense/selection.html')


def contact(request):
    return render_to_response('PetDispense/selection.html')


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
    #return render(request, "PetDispense/animals.html", {"Species": Species.objects.all()})


def breeds(request):
    table = BreedsTable(Breeds.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/breeds.html', {'table': table})
    #return render(request, "PetDispense/animals.html", {"Species": Species.objects.all()})


def species(request):
    table = SpeciesTable(Species.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/species.html', {'table': table})
    #return render(request, "PetDispense/animals.html", {"Species": Species.objects.all()})


class AnimalList(ListView):
    queryset = AnimalInfo.objects.order_by('+animal_name')


















