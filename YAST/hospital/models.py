# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractUser
from itertools import chain
from django.db.models import Q
from random import randint

# Create your models here.
class donor_predict(models.Model):
    OP_ID = models.IntegerField(primary_key=True)
    AGE = models.IntegerField()
    OCCUPATION = models.CharField(max_length = 100)
    GENDER = models.CharField(max_length = 100)
    MARRIED = models.CharField(max_length = 100)
    ZIP = models.CharField(max_length = 100,default="84511")
    ADDRESS = models.CharField(max_length = 100,default="Blanding")    
    CITY = models.CharField(max_length = 100)
    STATE = models.CharField(max_length = 120,default="Utah") 
    LONGITUDE = models.CharField(max_length = 100,default="109.4259")
    LATITUDE = models.CharField(max_length = 100,default="37.5617")    
    COUNTRY = models.CharField(max_length = 100)
    CHANNEL = models.CharField(max_length = 100)
    CONTACT = models.CharField(max_length = 100)
    EMAIL = models.CharField(max_length = 100)    
    EDU_LEVEL = models.CharField(max_length = 100)
    FAMILY_MEM = models.CharField(max_length = 100)
    TOTAL_HISTORICAL_DON = models.CharField(max_length = 100)
    LAST_DONATED = models.CharField(max_length = 100)
    OTHER_DONATION =  models.CharField(max_length = 100)
    WEIGHT = models.FloatField()
    HEIGHT = models.FloatField()
    BLOOD_GROUP = models.CharField(max_length = 100)
    NET_SCORE = models.FloatField()
    NET_RANK = models.IntegerField()
    TARGET_STATUS = models.CharField(max_length = 100)
    
    def __str__(self):
       return '%s (%s)' % (str(self.OP_ID),self.BLOOD_GROUP)
       
       
class hospital_info(models.Model):
    HOSPITAL_ID = models.IntegerField(primary_key=True)
    CHAIN_ID = models.IntegerField()
    HOSPITAL_NAME = models.CharField(max_length = 100)
    CHAIN_NAME = models.CharField(max_length = 100)
    ZIP = models.CharField(max_length = 100)
    ADDRESS = models.CharField(max_length = 100)
    CITY = models.CharField(max_length = 100)
    STATE = models.CharField(max_length = 120)
    COUNTRY = models.CharField(max_length = 100)
    LONGITUDE = models.CharField(max_length = 100)
    LATITUDE = models.CharField(max_length = 100)
    CONTACT_NO = models.CharField(max_length = 100)
    EMAIL = models.CharField(max_length = 100)   
    HOSPITAL_OWNERSHIP = models.CharField(max_length = 100)   
    HOSPITAL_TYPE = models.CharField(max_length = 100)       
    BLOOD_COLL_FACILITY = models.CharField(max_length = 100)
    APositive = models.IntegerField()
    ABPositive = models.IntegerField()
    OPositive = models.IntegerField()
    BPositive = models.IntegerField()
    ANegative = models.IntegerField()
    ABNegative = models.IntegerField()
    ONegative = models.IntegerField()
    BNegative = models.IntegerField()
    APositiveExpected = models.IntegerField(default=10)
    ABPositiveExpected = models.IntegerField(default=11)
    OPositiveExpected = models.IntegerField(default=12)
    BPositiveExpected = models.IntegerField(default=8)
    ANegativeExpected = models.IntegerField(default=13)
    ABNegativeExpected = models.IntegerField(default=18)
    ONegativeExpected = models.IntegerField(default=9)
    BNegativeExpected = models.IntegerField(default=7)    
    TOTAL_BEDS = models.IntegerField()
    SPECIALITY = models.CharField(max_length = 100)
    STAFF_COUNT = models.IntegerField()
    DOCTOR_COUNT = models.IntegerField()
    FOOTFALL = models.IntegerField()


    
    def __str__(self):
       return '%s (%s)' % (str(self.HOSPITAL_NAME),self.CITY)       
       
       
class blood_bank_master(models.Model):
    BLOOD_ID = models.IntegerField(primary_key=True)
    HOSPITAL_ID = models.ForeignKey(hospital_info,on_delete=models.CASCADE,default=1)
    DONOR_OP_ID = models.ForeignKey(donor_predict,on_delete=models.CASCADE,default=102)
    BLOOD_QTY = models.FloatField()
    DONATION_DATE = models.CharField(max_length = 100)
    DONATION_TIME = models.CharField(max_length = 100)
    BLOOD_STATUS = models.CharField(max_length = 100)
    SYSPHILIS = models.CharField(max_length = 100)
    HIV_POS = models.CharField(max_length = 100)
    HEPATITUS_POS = models.CharField(max_length = 100)
    OTHER_DISEASE = models.CharField(max_length = 100)
    BLOOD_COLL_METHOD = models.CharField(max_length = 100)
    BLOOD_DON_TYPE = models.CharField(max_length = 100)    
    BLOOD_INTEND_USE = models.CharField(max_length = 100)    
    def __str__(self):
       return '%s' % (str(self.BLOOD_ID))              

def GetDonorPredict():
    try:
        donor_object = donor_predict.objects.all().order_by('NET_RANK')
    except donor_predict.DoesNotExist:
        donor_object = None
    return donor_object    
    
def GetHospitalDetails(hospitalId):
    try:
        hosp_object = hospital_info.objects.get(HOSPITAL_ID=hospitalId)
    except hospital_info.DoesNotExist:
        hosp_object = None
    return hosp_object   
    

def GetChainHospitalDetails(chainId):
    try:
        hosp_object = hospital_info.objects.filter(CHAIN_ID=chainId)
    except hospital_info.DoesNotExist:
        hosp_object = None
    return hosp_object   
        
    
def GetBloodDonorDataforHospId(hospitalId):    
    try:
        blood_master = blood_bank_master.objects.filter(HOSPITAL_ID=hospitalId)
        don_data = donor_predict.objects.filter(blood_bank_master__HOSPITAL_ID=hospitalId);
        #data = donor_predict.objects.filter(HOSPITAL_ID=hospitalId).select_related('blood_bank_master')
        data = chain(blood_master,don_data)
    except blood_bank_master.DoesNotExist:
        data = None
    except donor_predict.DoesNotExist:
        data = None
    return data  
    
def getAllHospitals(COUNTRY):
    try:
       hosp_data = hospital_info.objects.filter(COUNTRY=COUNTRY); 
    except hospital_info.DoesNotExist:
        hosp_data = None
    return hosp_data    
    
def getAllHospitals(COUNTRY):
    try:
       hosp_data = hospital_info.objects.filter(COUNTRY=COUNTRY); 
    except hospital_info.DoesNotExist:
        hosp_data = None
    return hosp_data        

def getRightDonors(COUNTRY):
    try:
       donar_data = donor_predict.objects.filter(COUNTRY=COUNTRY).order_by('NET_RANK'); 
    except donor_predict.DoesNotExist:
        donar_data = None
    return donar_data    


    
def GetBloodDonorDataforReward(hospitalId):    
    try:
        blood_master = blood_bank_master.objects.filter(HOSPITAL_ID=hospitalId)
        don_data = donor_predict.objects.filter(blood_bank_master__HOSPITAL_ID=hospitalId).order_by('-TOTAL_HISTORICAL_DON')[:5];
    except blood_bank_master.DoesNotExist:
        don_data = None
    except donor_predict.DoesNotExist:
        don_data = None
    return don_data    
    
    