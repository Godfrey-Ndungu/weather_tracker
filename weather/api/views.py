from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import WeatherSerializer

from api.weather import WeatherAPI

@api_view(['GET'])
def weather_temperatures(request,city):
    """
    This is a  view function for registering get request and returning city temperature data in json format
    
    Parameters:
        city (str): The city to be queried.
    Returns:
        success:status_code (int): The request status code.
                response(dic): This has maximum.minimum,average and median value
        notsuccess:
                status_code (int): The request status code.
                response(dic): Error Message
        
    """
    if request.method == 'GET':
        try:
            days = request.GET["days"]
        except :
            return Response('Please Include days as query parameter',status=status.HTTP_406_NOT_ACCEPTABLE)

        # check that days are in number format
        try:
            days_value = int(days)
        except ValueError:
            return Response('Days should be an integer',status=status.HTTP_406_NOT_ACCEPTABLE)
            
        weather_api = WeatherAPI()
        weather_report = weather_api.get_city_weather_forecast_for_specific_days(city,days)
        
        status_code = weather_report[0]

        if status_code!= 200:
            return Response(weather_report[1],status=status_code)
        else:        
            weather_report_data = weather_report[1]
            serializer = WeatherSerializer(weather_report_data)
            # add custom partial content since api only support upto 14 days of weather forecast
            if int(days) > 14:
                return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
            else:
                return Response(serializer.data)
