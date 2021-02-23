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
        logger.info("REQUEST DATA {}".format(request.__dir__()))
        logger.info("REQUEST DATA {}".format(request.data))
        logger.info("REQUEST DATA {}".format(dict(request.data)))
        request_object = VGSRequest.objects.create(response=request.data)
        data = VGSRequestSerializer(request_object)
        return Response(data.data, status=status.HTTP_200_OK)
