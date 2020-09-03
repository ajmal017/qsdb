from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ES', views.ESViewSet)
router.register(r'RTY', views.RTYViewSet)
router.register(r'SI', views.SIViewSet)
router.register(r'QI', views.QIViewSet)
router.register(r'QO', views.QOViewSet)
router.register(r'PA', views.PAViewSet)
router.register(r'YM', views.YMViewSet)
router.register(r'PL', views.PLViewSet)
router.register(r'ZS', views.ZSViewSet)
router.register(r'GC', views.GCViewSet)
router.register(r'M6', views.M6ViewSet)
router.register(r'DY', views.DYViewSet)
router.register(r'CL', views.CLViewSet)
router.register(r'NG', views.NGViewSet)
router.register(r'MES', views.MESViewSet)
router.register(r'MNQ', views.MNQViewSet)
router.register(r'M2K', views.M2KViewSet)
router.register(r'MGC', views.MGCViewSet)
router.register(r'MYM', views.MYMViewSet)
router.register(r'QM', views.QMViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]