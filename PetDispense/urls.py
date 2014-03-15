from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    #url(r'^index/$', 'PetDispense.views.index', name=u"home"),
    url(r'^$',  'PetDispense.views.index', name=u"home"),
    url(r'^$',  'PetDispense.views.base', name=u"base"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)