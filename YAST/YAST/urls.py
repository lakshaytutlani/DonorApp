"""YAST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from login.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, name = 'login'),
    url(r'^signup/', signup, name = 'signup'),
    url(r'^cuDashboard/', cuDashboard, name = 'cuDashboard'),
    url(r'^cuNeedBlood/', cuNeedBlood, name = 'cuNeedBlood'),
    url(r'^cuVolunteer/', cuVolunteer, name = 'cuVolunteer'),
    url(r'^resetUser/', resetUser, name = 'resetUser'),
    url(r'^accounts/reset/(\d+)/(\d+)/$', reset_password, name='reset_password'), 
    
    ##Hospital UI
    url('hospital/', include('hospital.urls')),
    
    ##CHAIN ADMIN UI
    url('chainAdmin/', include('chainAdmin.urls')),
    
    url(r'^', homePage, name = ''),
]
