from django.conf.urls import url

from status.views import home
from status.views import api
from status.views import activity
from status.views import osd_details

urlpatterns = [
    url(r'^$', home),
    url(r'^api/$', api),
    url(r'^osd/(\d+)/$', osd_details),
    url(r'^activity/$', activity),
    
]
