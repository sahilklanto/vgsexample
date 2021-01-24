from django.urls.resolvers import URLPattern
from api.serializers import CardDataModelSerializer
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()

router.register('card-data', views.CardDataModelViewSet, basename='card-data')

urlpatterns = []

urlpatterns += router.urls