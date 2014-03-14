from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    #url(r'^index/$', 'PetDispense.views.index', name=u"home"),
    url(r'^$',  'PetDispense.views.index', name=u"home"),
)