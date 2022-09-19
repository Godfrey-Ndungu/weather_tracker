from django.urls import path

from .views import weather_temperatures

app_name='api'

urlpatterns = [
        path('api/locations/<city>/',weather_temperatures,name="weather_detail")
]

