from django.test import TestCase
from rest_framework.test import APIRequestFactory
from unittest import mock

import requests

from django.urls import reverse


class CityWeatherStatisticsAPITestCase(TestCase):

    def test_weather_retrieve(self):
        headers = {"days":12}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,200)

    def test_weather_retrieve_without_days(self):
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}))
        self.assertEqual(request.status_code,406)

    def test_weather_retrieve_days_not_number(self):
        headers = {"days":'not_number'}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,406)

    def test_weather_api_for_non_exisiting_city(self):
        headers = {"days":12}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'none_existing'}),headers)
        self.assertNotEqual(request.status_code,200)

    def test_days_greater_than_fourteen(self):
        headers = {"days":21}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,206)