import requests
import statistics
from decouple import config


WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
WEATHER_API_KEY = config('WEATHER_API_KEY')


class WeatherAPI():
    """
    This is a class for accessing weather api and processing the data into required information.
      
    Attributes:
        base_url(str): The base url accessing weather forecast in json format.
        api_key(str): The api key for accessing weatherapi.
    """

    def __init__(self, base_url=WEATHER_API_BASE_URL, api_key=WEATHER_API_KEY):
        self.base_url = base_url
        self.api_key = api_key

    def _get_city_weather_forecast_for_specific_days(self,city,days):
        """
        This is a function for getting weather forecast data for a specific city for a number of days.
        The Weather API offers a maximum number of days to be queried as 14.
        
        Parameters:
            city (str): The city to be queried.
            days (in): Number of days for forecast.
          
        Returns:
            success:status_code (int): The request status code.
                    maximum (dic): Maximum temperature for given days.
                    minimum(dic): Minimum temperature for given days.
                    median (dic): Median temperature for given days.
                    average (dic): Average temperature for given days at 2 decimal points.
            notsuccess:
                    status_code (int): The request status code.
                    error(dic):Error infromation from weather API
                    
            
        """
        
        # Request forecast for a particluar city for certain days
        payload = {'key': self.api_key, 'q':city,'days':days}
        response = requests.get(self.base_url,params=payload)
        status_code = response.status_code
        data = response.json()

        if status_code != 200:
            return status_code ,data['error'] ;

        else:
            forecast = data['forecast']
            temperatures=[]

            #loop throught the days to get daily data 
            for day in forecast['forecastday']:
                day_temperatures=(day['day'])
                temperatures.append(day_temperatures['maxtemp_c'])
                temperatures.append(day_temperatures['mintemp_c'])
            
            maximum_temperature = max(temperatures)
            minimum_temperature = min(temperatures)
            average_temperature = round(statistics.mean(temperatures),2) 
            median_temperature = statistics.median(temperatures)
    
            temperature_values = {"maximum":maximum_temperature, 
                                    "minimum": minimum_temperature,
                                    "average":average_temperature, 
                                    "median":median_temperature}

        return status_code ,temperature_values ;