from django.shortcuts import get_object_or_404, render, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django_tables2 import RequestConfig
from PetDispense.models import Species
from PetDispense.tables import SpeciesTable
from PetDispense.models import AnimalInfo
from PetDispense.tables import AnimalInfoTable


def index(request):
    return render(request, 'PetDispense/index.html')


def selection(request):
    return render('PetDispense/selection.html')


def contact(request):
    return render('PetDispense/selection.html')


def about(request):
    return render('PetDispense/about.html')


def agreement(request):
    return render('PetDispense/agreement.html')


def confirm(request):
    return render('PetDispense/confirm.html')


def returns(request):
    return render('PetDispense/returns.html')


def pin(request):
    return render('PetDispense/pin.html')


def animal(request):
    table = AnimalInfoTable(AnimalInfo.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'PetDispense/animals.html', {'table': table})
    #return render(request, "PetDispense/animals.html", {"Species": Species.objects.all()})