from django.conf.urls import url, include
from django.contrib import admin
from common import settings
from django.views import static
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('community.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,{'document_root':settings.STATIC_ROOT}),
]

handler400 = 'community.views.error_400'
handler403 = 'community.views.error_403'
handler404 = 'community.views.error_404'
handler500 = 'community.views.error_500'