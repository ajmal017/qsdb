from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import IBPricesModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class IBPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IBPricesModel
        fields = ['symbol', 'date', 'last', 'volume']