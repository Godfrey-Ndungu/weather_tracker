from django.test import TestCase

from api.weatherapi import WeatherAPI

from faker import Faker
fake = Faker()

class WeatherAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_init_method_variables_are_none(self):
        api = WeatherAPI()
        self.assertEqual(api.api, None)
        self.assertEqual(api.api_key, None)
        
    def test_init_method_variables_are_none(self):
        city=fake.text()
        days=12
        api = WeatherAPI(city,days)
        self.assertEqual(api.api, city)
        self.assertEqual(api.api_key, days)

    