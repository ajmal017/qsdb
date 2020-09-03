from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import *
from api.models import *
from api.services import *
from api.filters import *
import asyncio

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ESViewSet(viewsets.ModelViewSet):
    queryset = ESModel.objects.all()
    serializer_class = ESSerializer
    filterset_class = ESFilter
    
class RTYViewSet(viewsets.ModelViewSet):
    queryset = RTYModel.objects.all()
    serializer_class = RTYSerializer
    filterset_class = RTYFilter

class SIViewSet(viewsets.ModelViewSet):
    queryset = SIModel.objects.all()
    serializer_class = SISerializer
    filterset_class = SIFilter

class QIViewSet(viewsets.ModelViewSet):
    queryset = QIModel.objects.all()
    serializer_class = QISerializer
    filterset_class = QIFilter

class QOViewSet(viewsets.ModelViewSet):
    queryset = QOModel.objects.all()
    serializer_class = QOSerializer
    filterset_class = QOFilter
    
class PAViewSet(viewsets.ModelViewSet):
    queryset = PAModel.objects.all()
    serializer_class = PASerializer
    filterset_class = PAFilter
    
class YMViewSet(viewsets.ModelViewSet):
    queryset = YMModel.objects.all()
    serializer_class = YMSerializer
    filterset_class = YMFilter

class PLViewSet(viewsets.ModelViewSet):
    queryset = PLModel.objects.all()
    serializer_class = PLSerializer
    filterset_class = PLFilter

class ZSViewSet(viewsets.ModelViewSet):
    queryset = ZSModel.objects.all()
    serializer_class = ZSSerializer
    filterset_class = ZSFilter

class GCViewSet(viewsets.ModelViewSet):
    queryset = GCModel.objects.all()
    serializer_class = GCSerializer
    filterset_class = GCFilter

class M6ViewSet(viewsets.ModelViewSet):
    queryset = M6Model.objects.all()
    serializer_class = M6Serializer
    filterset_class = M6Filter
    
class DYViewSet(viewsets.ModelViewSet):
    queryset = DYModel.objects.all()
    serializer_class = DYSerializer
    filterset_class = DYFilter
    
class CLViewSet(viewsets.ModelViewSet):
    queryset = CLModel.objects.all()
    serializer_class = CLSerializer
    filterset_class = CLFilter

class NGViewSet(viewsets.ModelViewSet):
    queryset = NGModel.objects.all()
    serializer_class = NGSerializer
    filterset_class = NGFilter

class MESViewSet(viewsets.ModelViewSet):
    queryset = MESModel.objects.all()
    serializer_class = MESSerializer
    filterset_class = MESFilter

class MNQViewSet(viewsets.ModelViewSet):
    queryset = MNQModel.objects.all()
    serializer_class = MNQSerializer
    filterset_class = MNQFilter

class M2KViewSet(viewsets.ModelViewSet):
    queryset = M2KModel.objects.all()
    serializer_class = M2KSerializer
    filterset_class = M2KFilter

class MGCViewSet(viewsets.ModelViewSet):
    queryset = MGCModel.objects.all()
    serializer_class = MGCSerializer
    filterset_class = MGCFilter

class MYMViewSet(viewsets.ModelViewSet):
    queryset = MYMModel.objects.all()
    serializer_class = MYMSerializer
    filterset_class = MYMFilter
    
class QMViewSet(viewsets.ModelViewSet):
    queryset = QMModel.objects.all()
    serializer_class = QMSerializer
    filterset_class = QMFilter
    