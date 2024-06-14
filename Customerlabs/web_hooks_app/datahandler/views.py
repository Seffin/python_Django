from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from destinations.models import Destination
import requests

class IncomingDataHandler(APIView):
    def post(self, request):
        app_secret_token = request.headers.get('CL-X-TOKEN')

        if not app_secret_token:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=app_secret_token)
        except Account.DoesNotExist:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        for destination in account.destinations.all():
            headers = destination.headers
            if destination.http_method == 'GET':
                response = requests.get(destination.url, headers=headers, params=data)
            elif destination.http_method in ['POST', 'PUT']:
                response = requests.request(destination.http_method, destination.url, headers=headers, json=data)

        return Response({"message": "Data sent to destinations"}, status=status.HTTP_200_OK)