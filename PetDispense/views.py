from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from PetDispense.models import AnimalInfo


def index(request):
    return render_to_response('PetDispense/index.html')


def selection(request):
    return render_to_response('PetDispense/selection.html')


def about(request):
    return render_to_response('PetDispense/about.html')


def agreement(request):
    return render_to_response('PetDispense/agreement.html')


def confirm(request):
    return render_to_response('PetDispense/confirm.html')


def returns(request):
    return render_to_response('PetDispense/returns.html')


def pin(request):
    return render_to_response('PetDispense/pin.html')
