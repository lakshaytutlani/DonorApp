# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
import json
from collections import OrderedDict
from models import *
from django.http import JsonResponse
import json
import datetime
from django.utils import timezone
from login.distanceLongitudeLatitude import getLatitudeLongitude, getDistanceBetweenTwoPoints
from operator import itemgetter
from django.conf import settings
from datetime import date
from hospital.models import *



# Create your views here.

path = getattr(settings, "CSV_FOLDER", None) +'CountryToCodeMapping.csv'
CountryToCodeMappingFile = open(path, "r")
CountryToCodeMapping = {}
for rows in CountryToCodeMappingFile:
    rows = rows[0:-1].decode('UTF-8')
    fullForm, ShortForm = rows.split("|")
    CountryToCodeMapping[fullForm] = ShortForm
    
    
def chDashboard(request):   
    dummy = "chain_1"
    chain_id = int(dummy.split("_")[-1])
    rows_hosp_list = GetChainHospitalDetails(chain_id)

    return render(request, 'chDashboard.html', {"data_hosp":rows_hosp_list})    