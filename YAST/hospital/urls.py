from django.conf.urls import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^topDonors/', views.topDonors, name='topDonors'),
    url(r'^dashboard/', views.hpDashboard, name='hpDashboard'),
    url(r'^bloodMonitor/', views.hpbloodMonitor, name='hpbloodMonitor'),
    url(r'^sendemail/', views.sendemail, name='topDonors'),
    url(r'^reward/', views.reward, name='reward'),
    url(r'^network/', views.network, name='network'),
    url(r'^hospitalCountry/(\D+)/', views.getHospitals),
    url(r'^getDonorHospitalId/(\d+)/', views.getAllDonorHospitalId),
    url(r'^addDonationEntry/', views.addDonationEntry),
    url(r'^stockadd/(\d+)/', views.updatestocks)
]

urlpatterns = format_suffix_patterns(urlpatterns)