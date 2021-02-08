from django.urls import path
from portal import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='portal')
]
