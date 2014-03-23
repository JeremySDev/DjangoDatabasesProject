from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import DetailView, ListView
from PetDispense.views import AnimalList, \
    AgeList, OwnerList, MedInfoList, BasicInfoList, BasicInfo2List,\
    ShelterSickList, YoungestList, AgeSortList, CatDogList, CountInShelterList

urlpatterns = patterns('',
                       url(r'^$', 'PetDispense.views.index', name=u"home"),
                       url(r'^index/$', 'PetDispense.views.index', name=u"home"),
                       url(r'^selection/$', 'PetDispense.views.selection', name=u"selection"),
                       url(r'^about/$', 'PetDispense.views.about', name=u"about"),
                       url(r'^agreement/$', 'PetDispense.views.agreement', name=u"agreement"),
                       url(r'^confirm/$', 'PetDispense.views.confirm', name=u"confirm"),
                       url(r'^pin/$', 'PetDispense.views.pin', name=u"pin"),
                       url(r'^returns/$', 'PetDispense.views.returns', name=u"returns"),
                       url(r'^animal$', 'PetDispense.views.animal', name=u"animal"),
                       url(r'^breeds$', 'PetDispense.views.breeds', name=u"breeds"),
                       url(r'^species$', 'PetDispense.views.species', name=u"species"),
                       url(r'^contact/$', 'PetDispense.views.contact', name=u"contact"),
                       url(r'^query0/$', AnimalList.as_view()),
                       url(r'^query1/$', AgeList.as_view()),
                       url(r'^query2/$', OwnerList.as_view()),
                       url(r'^query3/$', MedInfoList.as_view()),
                       url(r'^query4/$', BasicInfoList.as_view()),
                       url(r'^query5/$', BasicInfo2List.as_view()),
                       url(r'^query6/$', ShelterSickList.as_view()),
                       url(r'^query7/$', YoungestList.as_view()),
                       url(r'^query8/$', AgeSortList.as_view()),
                       url(r'^query9/$', CatDogList.as_view()),
                       url(r'^query10/$', CountInShelterList.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)