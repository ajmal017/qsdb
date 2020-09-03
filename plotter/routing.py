from django.urls import re_path
from plotter import consumers

websocket_urlpatterns = [
    re_path(r'ws/plotter/(?P<stock_name>\w+)/$', consumers.PlotterConsumer),
]