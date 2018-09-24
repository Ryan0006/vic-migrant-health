from django.conf.urls import url, include
from django.contrib import admin
from common import settings
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('community.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,{'document_root':settings.STATIC_ROOT}),
]
