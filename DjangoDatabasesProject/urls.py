from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('PetDispense.urls')),
                       #url(r'^$', 'PetDispense.urls'),
                       #url(r'^$', include('PetDispense.urls')),
                       #url(r'^PetDispense/', include('PetDispense.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
