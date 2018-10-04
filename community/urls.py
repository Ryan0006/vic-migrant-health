from django.conf.urls import url
from . import views

app_name = 'community'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^findsuburb/$', views.findsuburb, name='findsuburb'),
    url(r'^search/$', views.search_suburb, name='search'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^map/$', views.map, name='map'),
    url(r'^aboutus/$', views.about_us, name='aboutus'),
    url(r'^result/$', views.search_result, name='result'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^sendemail/$', views.sendemail, name='sendemail'),
    url(r'^immunization/$', views.immunization, name='immunization'),
    # url(r'^compare/chart/$', views.ChartData.as_view()),
    url(r'^visualization/$', views.visualization, name='visualization'),
    # url(r'^readCommunity/$', views.readCommunity, name='readCommunity'),
    # url(r'^readLanguage/$', views.readLanguage, name='readLanguage'),
    # url(r'^readCountry/$', views.readCountry, name='readCountry'),
    # url(r'^readSuburbLocation/$', views.readSuburbLocation, name='readSuburbLocation'),
    # url(r'^readSchool/$', views.readSchool, name='readSchool'),
    # url(r'^readHospital/$', views.readHospital, name='readHospital'),
]