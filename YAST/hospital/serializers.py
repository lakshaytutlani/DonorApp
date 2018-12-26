from .models import *
from rest_framework import serializers


class DonorMaster(serializers.Serializer):
    BLOOD_ID = serializers.IntegerField()
    BLOOD_QTY = serializers.FloatField()
    DONATION_DATE = serializers.CharField(max_length = 100)
    DONATION_TIME = serializers.CharField(max_length = 100)
    BLOOD_STATUS = serializers.CharField(max_length = 100)
    SYSPHILIS = serializers.CharField(max_length = 100)
    HIV_POS = serializers.CharField(max_length = 100)
    HEPATITUS_POS = serializers.CharField(max_length = 100)
    OTHER_DISEASE = serializers.CharField(max_length = 100)
    BLOOD_COLL_METHOD = serializers.CharField(max_length = 100)
    BLOOD_DON_TYPE = serializers.CharField(max_length = 100)    
    BLOOD_INTEND_USE = serializers.CharField(max_length = 100)      

    def create(self, validated_data):
        return blood_bank_master.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.BLOOD_ID = validated_data.get('BLOOD_ID', instance.BLOOD_ID)
        instance.BLOOD_QTY = validated_data.get('BLOOD_QTY', instance.BLOOD_QTY)  
        instance.DONATION_DATE = validated_data.get('DONATION_DATE', instance.DONATION_DATE)          
        instance.DONATION_TIME = validated_data.get('DONATION_TIME', instance.DONATION_TIME)
        instance.BLOOD_STATUS = validated_data.get('BLOOD_STATUS', instance.BLOOD_STATUS)
        instance.SYSPHILIS = validated_data.get('SYSPHILIS', instance.SYSPHILIS)
        instance.HIV_POS = validated_data.get('HIV_POS', instance.HIV_POS)           
        instance.HEPATITUS_POS = validated_data.get('HEPATITUS_POS', instance.HEPATITUS_POS)   
        instance.OTHER_DISEASE = validated_data.get('OTHER_DISEASE', instance.OTHER_DISEASE)
        instance.BLOOD_COLL_METHOD = validated_data.get('BLOOD_COLL_METHOD', instance.BLOOD_COLL_METHOD)
        instance.BLOOD_DON_TYPE = validated_data.get('BLOOD_DON_TYPE', instance.BLOOD_DON_TYPE)
        instance.BLOOD_INTEND_USE = validated_data.get('BLOOD_INTEND_USE', instance.BLOOD_INTEND_USE)         
        instance.save()
        return instance    
        
        
class HospitalMaster(serializers.Serializer):
    HOSPITAL_ID = serializers.IntegerField()
    CHAIN_ID = serializers.IntegerField()
    HOSPITAL_NAME = serializers.CharField(max_length = 100)
    CHAIN_NAME = serializers.CharField(max_length = 100)
    ZIP = serializers.CharField(max_length = 100)
    ADDRESS = serializers.CharField(max_length = 100)
    CITY = serializers.CharField(max_length = 100)
    STATE = serializers.CharField(max_length = 120)
    COUNTRY = serializers.CharField(max_length = 100)
    
    def create(self, validated_data):
        return hospital_info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.HOSPITAL_ID = validated_data.get('HOSPITAL_ID', instance.HOSPITAL_ID)
        instance.CHAIN_ID = validated_data.get('CHAIN_ID', instance.CHAIN_ID)
        instance.HOSPITAL_NAME = validated_data.get('HOSPITAL_NAME', instance.HOSPITAL_NAME)
        instance.CHAIN_NAME = validated_data.get('CHAIN_NAME', instance.CHAIN_NAME)
        instance.ZIP = validated_data.get('ZIP', instance.ZIP)
        instance.ADDRESS = validated_data.get('ADDRESS', instance.ADDRESS)
        instance.CITY = validated_data.get('CITY', instance.CITY)
        instance.STATE = validated_data.get('STATE', instance.STATE)
        instance.COUNTRY = validated_data.get('COUNTRY', instance.COUNTRY)
        instance.save()
        return instance    
            
        
class HospitalMaterStock(serializers.Serializer):
    HOSPITAL_ID = serializers.IntegerField()
    APositive = serializers.IntegerField()
    ABPositive = serializers.IntegerField()
    OPositive = serializers.IntegerField()
    BPositive = serializers.IntegerField()
    ANegative = serializers.IntegerField()
    ABNegative = serializers.IntegerField()
    ONegative = serializers.IntegerField()
    BNegative = serializers.IntegerField()        
    
    def create(self, validated_data):
        return hospital_info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.HOSPITAL_ID = validated_data.get('HOSPITAL_ID', instance.HOSPITAL_ID)
        instance.APositive = validated_data.get('APositive', instance.APositive)
        instance.ABPositive = validated_data.get('ABPositive', instance.ABPositive)
        instance.OPositive = validated_data.get('OPositive', instance.OPositive)
        instance.BPositive = validated_data.get('BPositive', instance.BPositive)
        instance.ANegative = validated_data.get('ANegative', instance.ANegative)
        instance.ABNegative = validated_data.get('ABNegative', instance.ABNegative)
        instance.ONegative = validated_data.get('ONegative', instance.ONegative)
        instance.BNegative = validated_data.get('BNegative', instance.BNegative)
        instance.save()
        return instance    
   