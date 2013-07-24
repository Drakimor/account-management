from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    # Example:

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^list$', 'list'),
    (r'^process$', 'process'),
    (r'^api_list$', 'api_list'),
    (r'^api_process$', 'api_process'),
    (r'^api_process_update$', 'api_process_update'),

)
