from django.urls.resolvers import URLPattern
from api.serializers import CardDataModelSerializer
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()

router.register('card-data', views.CardDataModelViewSet, basename='card-data')

urlpatterns = [
    path('reveal-data', views.RevealData.as_view(), name='reveal-data'),
    path('tokenize-image', views.TokenizeImage.as_view(), name='tokenize-image'),
    path('temp', views.Temp.as_view(), name='temp')
]

urlpatterns += router.urls
