from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('plotter/', include('plotter.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', include('api.urls')),
]
