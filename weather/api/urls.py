from django.urls import path

from .views import city_weather_statistics

app_name='api'

urlpatterns = [
        path('api/locations/<city>/',city_weather_statistics,name="weather_detail")
]
