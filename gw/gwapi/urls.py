from django.conf.urls.defaults import *

urlpatterns = patterns('gwapi.views',
                       (r'^get_countries','get_countries'),
                       (r'^get_country','get_country'),
                    )
    
                       
