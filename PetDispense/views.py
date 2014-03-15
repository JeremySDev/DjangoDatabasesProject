from django.shortcuts         import get_object_or_404, render_to_response
from django.http              import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template          import RequestContext
from PetDispense.models import AnimalInfo


def index(request):
    return render_to_response('PetDispense/index.html')


def base(request):
    return render_to_response('PetDispense/base.html')