import requests
import statistics
from decouple import config


WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
WEATHER_API_KEY = config('WEATHER_API_KEY')


class WeatherAPI(object):

    def __init__(self, api=WEATHER_API_BASE_URL, api_key=WEATHER_API_KEY):
        self.api = api
        self.api_key = api_key

    def _get_city_weather_forecast_for_specific_days(self,city,days):
        # Request forecast for a particluar city for certain days
        payload = {'key': self.api_key, 'q':city,'days':days}
        response = requests.get(self.api,params=payload)
        status_code = response.status_code
        data = response.json()
        forecast = data['forecast']
        temperatures=[]

        #loop throught the days to get daily data 
        for day in forecast['forecastday']:
            day_temperatures=(day['day'])
            temperatures.append(day_temperatures['maxtemp_c'])
            temperatures.append(day_temperatures['mintemp_c'])
        
        maximum_temperature = max(temperatures)
        minimum_temperature = min(temperatures)
        average_temperature = statistics.mean(temperatures) 
        median_temperature = statistics.median(temperatures)
 
        temperature_values = {"maximum":maximum_temperature, "minimum": minimum_temperature,"average":average_temperature, "median":median_temperature}

        return status_code ,temperature_values ;