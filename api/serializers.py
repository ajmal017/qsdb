from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class  ESSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESModel
        fields = ['Date', 'Last', 'Volume']
        
class  RTYSerializer(serializers.ModelSerializer):
    class Meta:
        model = RTYModel
        fields = ['Date', 'Last', 'Volume']
        
class  SISerializer(serializers.ModelSerializer):
    class Meta:
        model = SIModel
        fields = ['Date', 'Last', 'Volume']
        
class  QISerializer(serializers.ModelSerializer):
    class Meta:
        model = QIModel
        fields = ['Date', 'Last', 'Volume']
        
class  QOSerializer(serializers.ModelSerializer):
    class Meta:
        model = QOModel
        fields = ['Date', 'Last', 'Volume']
        
class  PASerializer(serializers.ModelSerializer):
    class Meta:
        model = PAModel
        fields = ['Date', 'Last', 'Volume']

class  YMSerializer(serializers.ModelSerializer):
    class Meta:
        model = YMModel
        fields = ['Date', 'Last', 'Volume']
        
class  PLSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLModel
        fields = ['Date', 'Last', 'Volume']
        
class  ZSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZSModel
        fields = ['Date', 'Last', 'Volume']
        
class  GCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCModel
        fields = ['Date', 'Last', 'Volume']
        
class  M6Serializer(serializers.ModelSerializer):
    class Meta:
        model = M6Model
        fields = ['Date', 'Last', 'Volume']
        
class  DYSerializer(serializers.ModelSerializer):
    class Meta:
        model = DYModel
        fields = ['Date', 'Last', 'Volume']
        
class  CLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLModel
        fields = ['Date', 'Last', 'Volume']
        
class  NGSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGModel
        fields = ['Date', 'Last', 'Volume']

class  MESSerializer(serializers.ModelSerializer):
    class Meta:
        model = MESModel
        fields = ['Date', 'Last', 'Volume']
        
class  MNQSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNQModel
        fields = ['Date', 'Last', 'Volume']
        
class  M2KSerializer(serializers.ModelSerializer):
    class Meta:
        model = M2KModel
        fields = ['Date', 'Last', 'Volume']
        
class  MGCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MGCModel
        fields = ['Date', 'Last', 'Volume']
        
class  MYMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MYMModel
        fields = ['Date', 'Last', 'Volume']
        
class  QMSerializer(serializers.ModelSerializer):
    class Meta:
        model = QMModel
        fields = ['Date', 'Last', 'Volume']