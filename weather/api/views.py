from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import WeatherSerializer

from weather.weatherapi import WeatherAPI

class WeatherViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        weather_api = WeatherAPI()
        weather_report = weather_api._get_city_weather_forecast_for_specific_days('london',3)
        weather_report_data = weather_report[1]
        serializer = WeatherSerializer(weather_report_data)
        
        return Response(serializer.data)