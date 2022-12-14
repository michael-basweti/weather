import requests
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from WeatherProject.settings import WEATHER_API_BASE_URL, WEATHER_API_KEY
from utils import average
import statistics

# an endpoint to test whether the api is running
class index(APIView):

    def get(self, request):
        message = {
            "message":"Hello, this API returns data"
        }

        return Response(message, status=status.HTTP_200_OK)


class WeatherStats(APIView):

    def get(self, request):
        city = request.query_params.get('city')
        days = request.query_params.get('days')
        # weather api url
        api_URL = "{}key={}&q={}&days={}".format(WEATHER_API_BASE_URL,WEATHER_API_KEY,city,days)
        # get data from weather api
        raw_stats = requests.get(api_URL)
        stats = raw_stats.json()
        
        if "error" in stats:
            # return error message to the user
            return Response(stats['error'], status=status.HTTP_404_NOT_FOUND)
        else:

            # The whole process below is to extract the data we get back so that we remain with the required data only
            day_forecasts = stats['forecast']['forecastday']

            day_temp_objects = []
            average_daily_temps = []

            for day_temps in day_forecasts:
                day_temp_objects.append(day_temps['day'])

            for day_temp_object in day_temp_objects:
                # weather api returns temperature in celcius and fahrenheit, here we pick celcius.
                average_daily_temps.append(day_temp_object['avgtemp_c'])

            period_stats = {
                "maximum": max(average_daily_temps),
                "minimum": min(average_daily_temps),
                "average": average(average_daily_temps),
                "median": statistics.median(average_daily_temps),
            }

            return Response(period_stats, status=status.HTTP_200_OK)