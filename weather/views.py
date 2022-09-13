import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class index(APIView):

    def get(self, request):
        message = {
            "message":"Hello, this API returns data"
        }

        return Response(message, status=status.HTTP_200_OK)