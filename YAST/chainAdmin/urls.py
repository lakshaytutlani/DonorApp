from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^chDashboard/', views.chDashboard, name='chDashboard')
]