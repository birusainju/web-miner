from django.conf.urls.defaults import *
from webMiner.search.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import os
media=os.path.join(
  os.path.dirname(__file__), 'media'
)
urlpatterns = patterns('',
    # Example:
    # (r'^webMiner/', include('webMiner.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
	url(r'^$', searcher,name="home_page"),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': media }),
	
)
