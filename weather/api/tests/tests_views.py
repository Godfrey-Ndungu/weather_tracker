from django.test import TestCase
from rest_framework.test import APIRequestFactory
from unittest import mock

import requests

from django.urls import reverse


class WeatherAPITestCase(TestCase):

    def test_weather_retrieve(self):
        headers = {"days":12}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,200)

       

