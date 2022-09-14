from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from weather.views import index, WeatherStats


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, index)

    def test_weather_stats_url_resolves(self):
        url = reverse('location-stats')
       
        self.assertEqual(resolve(url).func.view_class, WeatherStats)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_weather_request(self):
        url = reverse('location-stats')
        paramsurl = url+"?city=london&days=2"
        response = self.client.get(paramsurl)
        self.assertEquals(response.status_code, 200)

    def test_successful_index_request(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_location_not_exist(self):
        url = reverse('location-stats')
        paramsurl = url+"?city=lo&days=2"
        response = self.client.get(paramsurl)
        self.assertEquals(response.status_code, 404)
