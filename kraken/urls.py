from django.conf.urls import url

from status.views import home
from status.views import api
from status.views import activity
from status.views import osd_details
from ops.views import ops
from ops.views import user_custom

urlpatterns = [
    url(r'^$', home),
    url(r'^ops/$', ops),
    url(r'^api/$', api),
    url(r'^osd/(\d+)/$', osd_details),
    url(r'^activity/$', activity),
    url(r'^user/(.+?)(/.+?)?(/.+?)?/$', user_custom),
    
]
