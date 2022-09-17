from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import WeatherSerializer

class WeatherViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        weather_report_test = [{"maximum": 10, "minimum": 0,"average": 4, "median": 23}] 
        serializer = WeatherSerializer(weather_report_test)
        
        return Response(serializer.data)