# from django.test import TestCase

# from api.weatherapi import WeatherAPI

# from faker import Faker
# fake = Faker()

# class WeatherAPITestCase(TestCase):
#     def test_variables_returned_by_init_method(self):
#         city=fake.text()
#         days=12
#         api = WeatherAPI(city,days)
#         self.assertEqual(api.api, city)
#         self.assertEqual(api.api_key, days)

#     def test_city_weather_forecast_for_specific_days_method(self):
#         api_class = WeatherAPI()
#         api_method= api_class._get_city_weather_forecast_for_specific_days('london',12)
#         self.assertEqual(api_method[0],200)

#     def test_city_weather_forecast_for_city_not_existing_method(self):
#         api_class = WeatherAPI()
#         api_method= api_class._get_city_weather_forecast_for_specific_days('citynotavailable12',12)
#         self.assertNotEqual(api_method[0],200)
    
#     def test_city_weather_forecast_number_of_days_not_integer(self):
#         # if number of days not provided will use 0 as default
#         api_class = WeatherAPI()
#         api_method= api_class._get_city_weather_forecast_for_specific_days('london','number_of_days_string')
#         self.assertEqual(api_method[0],200)
    
#     def test_city_weather_forecast_number_of_days_not_integera_and_city_integer(self):
#         api_class = WeatherAPI()
#         api_method= api_class._get_city_weather_forecast_for_specific_days(12,'number_of_days_string')
#         self.assertNotEqual(api_method[0],200)
    
    
