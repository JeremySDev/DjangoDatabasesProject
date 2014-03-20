from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import DetailView, ListView

urlpatterns = patterns('PetDispense.views',
                       url(r'^index/$', 'index', name=u"home"),
                       url(r'^selection/$', 'selection', name=u"selection"),
                       url(r'^about/index.html$', 'index', name=u"about"),
                       url(r'^about/$', 'about', name=u"about"),
                       url(r'^agreement/$', 'agreement', name=u"agreement"),
                       url(r'^confirm/$', 'confirm', name=u"confirm"),
                       url(r'^pin/$', 'pin', name=u"pin"),
                       url(r'^returns$', 'returns', name=u"returns"),
                       url(r'^animal$', 'animal', name=u"animal"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)