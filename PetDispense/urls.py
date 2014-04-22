from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import DetailView, ListView l
from PetDispense.views import AnimalList, \
    AgeList, OwnerList, MedInfoList, BasicInfoList, BasicInfo2List, \
    ShelterSickList, YoungestList, AgeSortList, CatDogList, CountInShelterList

urlpatterns = patterns('',
                       url(r'^$', 'PetDispense.views.index', name=u"home"),
                       url(r'^index/$', 'PetDispense.views.index', name=u"home"),
                       url(r'^newuser/$', 'PetDispense.views.new_user', name=u"newuser"),
                       url(r'^login_failure/$', 'PetDispense.views.login_failure', name=u"login_failure"),
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
                       url(r'^query/$', 'PetDispense.views.query', name=u"query"),
                       url(r'^results/$', 'PetDispense.views.search', name=u"search"),
                       url(r'^results2/$', 'PetDispense.views.search_owners', name=u"search_owners"),
                       url(r'^query0/$', AnimalList.as_view(), name=u"query0"),
                       url(r'^query1/$', AgeList.as_view(), name=u"query1"),
                       url(r'^query2/$', OwnerList.as_view(), name=u"query2"),
                       url(r'^query3/$', MedInfoList.as_view(), name=u"query3"),
                       url(r'^query4/$', BasicInfoList.as_view(), name=u"query4"),
                       url(r'^query5/$', BasicInfo2List.as_view(), name=u"query5"),
                       url(r'^query6/$', ShelterSickList.as_view(), name=u"query6"),
                       url(r'^query7/$', YoungestList.as_view(), name=u"query7"),
                       url(r'^query8/$', AgeSortList.as_view(), name=u"query8"),
                       url(r'^query9/$', CatDogList.as_view(), name=u"query9"),
                       url(r'^query10/$', CountInShelterList.as_view(), name=u"query10"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)