from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import IBPricesSerializer, UserSerializer, GroupSerializer
from api.models import IBPricesModel
from api.services import *
# Create your views here.


class RequestDataViewSet(viewsets.ModelViewSet):
    queryset = request_data()

class IBPricesViewSet(viewsets.ModelViewSet):
    queryset = IBPricesModel.objects.all().order_by('date')
    serializer_class = IBPricesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]