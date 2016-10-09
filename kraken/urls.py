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



#from django.conf.urls.defaults import patterns, include, url
#
#base_urlpatterns = patterns(
#    '',
#    url(r'^$', 'status.views.home', name='home'),
#    url(r'^ops/$', 'ops.views.ops', name='ops'),
#    url(r'^osd/(\d+)/$', 'status.views.osd_details', name='osd_details'),
#    url(r'^activity/$', 'status.views.activity', name='activity'),
#    url(r'^user/(.+?)(/.+?)?(/.+?)?/$', 'ops.views.user_custom',
#        name='user_custom'),
#    url(r'^api/$', "status.views.api", name="api"),
#)
#
#urlpatterns = patterns('',
#    url(r'krakendash/', include(base_urlpatterns)),
#)
