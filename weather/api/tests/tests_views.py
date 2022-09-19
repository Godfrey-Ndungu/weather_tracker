from django.test import TestCase
from django.urls import reverse


class WeatherStatisticsAPITestCase(TestCase):

    def test_get_weather_data(self):
        headers = {"days":12}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,200)

    def test_get_weather_data_without_days(self):
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}))
        self.assertEqual(request.status_code,406)

    def test_get_weather_with_days_not_number(self):
        headers = {"days":'not_number'}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,406)

    def test_get_weather_data_for_non_exisiting_city(self):
        headers = {"days":12}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'none_existing'}),headers)
        self.assertNotEqual(request.status_code,200)

    def test_get_weather_data_for_days_greater_than_fourteen(self):
        headers = {"days":0}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,200)

    def test_get_weather_data_for_zero_days(self):
        headers = {"days":21}
        request = self.client.get(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertEqual(request.status_code,206)
    
    
    def test_send_post_request(self):
        headers = {"days":21}
        request = self.client.post(reverse('api:weather_detail', kwargs={'city':'london'}),headers)
        self.assertNotEqual(request.status_code,200)
    