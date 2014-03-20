from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
                       url(r'^index/$', 'PetDispense.views.index', name=u"home"),
                       url(r'^petdispense.herokuapp.com/$', 'PetDispense.views.index', name=u"home"),
                       url(r'^selection/$', 'PetDispense.views.selection', name=u"selection"),
                       url(r'^$', 'PetDispense.views.selection', name=u"selection"),
                       url(r'^about/index.html$', 'PetDispense.views.index', name=u"about"),
                       url(r'^about/$', 'PetDispense.views.about', name=u"about"),
                       url(r'^$', 'PetDispense.views.about', name=u"about"),
                       url(r'^agreement/$', 'PetDispense.views.agreement', name=u"agreement"),
                       url(r'^$', 'PetDispense.views.agreement', name=u"agreement"),
                       url(r'^confirm/$', 'PetDispense.views.confirm', name=u"confirm"),
                       url(r'^$', 'PetDispense.views.confirm', name=u"confirm"),
                       url(r'^pin/$', 'PetDispense.views.pin', name=u"pin"),
                       url(r'^$', 'PetDispense.views.pin', name=u"pin"),
                       url(r'^returns$', 'PetDispense.views.returns', name=u"returns"),
                       url(r'^$', 'PetDispense.views.returns', name=u"returns"),
                       url(r'^animal$', 'PetDispense.views.animal', name=u"animal"),
                       url(r'^$', 'PetDispense.views.animal', name=u"animal"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)