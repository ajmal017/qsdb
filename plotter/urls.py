from django.urls import path
from plotter import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:stock_name>/', views.stock, name='stock'),
]