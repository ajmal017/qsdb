from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import PASerializer, UserSerializer, GroupSerializer
from api.models import PAModel
from api.services import *
from api.filters import PAFilter
# Create your views here.

class PAViewSet(viewsets.ModelViewSet):
    queryset = PAModel.objects.all()
    serializer_class = PASerializer
    filterset_class = PAFilter
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]