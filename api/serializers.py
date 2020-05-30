from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import PAModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class  PASerializer(serializers.ModelSerializer):
    class Meta:
        model = PAModel
        fields = ['Date', 'Last', 'Volume']
