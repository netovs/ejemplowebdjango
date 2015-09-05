from django.conf.urls import patterns, include, url
from django.conf.urls.static import static



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from lweb import views





urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
   
    url(r'^lweb/', include('blatoso.urls')),
    url(r'^(?P<cat_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<tema_id>\d+)/tipo/$', views.tipo, name='tipo'), 
   
    
    # url(r'^admin/', include(admin.site.urls)),
    
    
) 