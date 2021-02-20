from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

routers = DefaultRouter()


urlpatterns = [
    path('log-request', views.LogRequest.as_view(), name='log-request')
]
