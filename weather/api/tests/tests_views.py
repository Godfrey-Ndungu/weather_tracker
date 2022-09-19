from django.test import TestCase
from rest_framework.test import APIRequestFactory

from api.views import WeatherViewSet

factory = APIRequestFactory()

class WeatherAPITestCase(TestCase):

    def test_weather_retrieve(self):
        request = self.client.get('http://localhost:8000/api/locations/london/?days=2')
        self.assertEqual(request.status_code,200)

    def test_view_set(self):
        request = factory.get('http://localhost:8000/api/locations/london/?days=2')
        view = WeatherViewSet.as_view({'get': 'retrieve'})
        response = view(request,'london')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,{'maximum': 17.9, 'minimum': 10.1, 'average': 13.9, 'median': 13.799999999999999})

    def test(self):
        request = factory.get('http://localhost:8000/api/locations/london/?days=2')
        weather=WeatherViewSet()
        response=weather.retrieve(request,'london')
        self.assertEqual(response.status_code,406)


