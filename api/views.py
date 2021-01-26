import os
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from portal.models import CardData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CardDataModelSerializer
import requests as r

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class CardDataModelViewSet(ModelViewSet):
    queryset = CardData.objects.all()
    serializer_class = CardDataModelSerializer
    authentication_classes = [CsrfExemptSessionAuthentication, ]


class RevealData(APIView):
    def get(self, request):
        print(request.data)
        return Response({}, status=status.HTTP_200_OK)


class TokenizeImage(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, ]
    def post(self, request):
        print(request.data)
        """
        curl https://ENDPOINT.COM -k -x
            <Username>:<Password>@<Vault-ID>.sandbox.verygoodproxy.com:8080
        """
        res = r.post("http://localhost:8000/api/v1/dummy-view")
        return Response({}, status=status.HTTP_200_OK)


class Temp(APIView):
    def post(self, request):
        print(request.data)
        res = r.get("http://localhost:8000/api/v1/dummy-view", data=dict(request.data))
        print(res.json())
        print(res)
        return Response({}, status=status.HTTP_200_OK)
