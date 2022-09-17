from django.urls import path

from .views import WeatherViewSet
app_name='api'

urlpatterns = [
        path('api/locations/<pk>/',WeatherViewSet.as_view({'get': 'retrieve'}),name="weather_detail")
]
