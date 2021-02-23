from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from api.models import VGSRequest
import logging

logger = logging.getLogger(__name__)

class VGSRequestSerializer(ModelSerializer):
    class Meta:
        model = VGSRequest
        fields = '__all__'


class LogRequest(APIView):
    def post(self, request):
        d = {}

        for key, value in request.data.items():
            print(value)
            print(value[0])
            d[key] = value[0]

        logger.info("asdfasdfasdf {}".format(d))

        request_object = VGSRequest.objects.create(response=dict(request.data))
        data = VGSRequestSerializer(request_object)
        return Response(data.data, status=status.HTTP_200_OK)
