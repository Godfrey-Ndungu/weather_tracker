from email.mime import base
from django.test import TestCase

from api.weather import WeatherAPI

from faker import Faker
fake = Faker()

class WeatherAPITestCase(TestCase):
    
    def test_variables_returned_by_init_method(self):
        base_url = 'http://testing.com'
        api_key = fake.text
        api = WeatherAPI(base_url,api_key)
        self.assertEqual(api.base_url,base_url)
        self.assertEqual(api.api_key,api_key)

    def test_weather_forecast_for_city_for_specific_days(self):
        weather = WeatherAPI()
        weather_data= weather.get_city_weather_forecast_for_specific_days('london',12)
        self.assertEqual(weather_data[0],200)

    def test_weather_forecast_for_nonexisting_city(self):
        weather = WeatherAPI()
        weather_data= weather.get_city_weather_forecast_for_specific_days('citynotavailable12',12)
        self.assertNotEqual(weather_data[0],200)
    
    def test_weather_forecast_days_not_integer(self):
        # if number of days not provided will use 0 as default
        weather = WeatherAPI()
        weather_data= weather.get_city_weather_forecast_for_specific_days('london','number_of_days_string')
        self.assertEqual(weather_data[0],200)
    
    def test_city_weather_forecast_number_of_days_not_number_and_city_name_is_number(self):
        weather = WeatherAPI()
        weather_data= weather.get_city_weather_forecast_for_specific_days(12,'number_of_days_string')
        self.assertNotEqual(weather_data[0],200)



    