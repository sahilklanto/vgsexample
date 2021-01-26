from django.urls import path
from portal import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('reveal', views.Reveal.as_view(), name='reveal'),
    path('tokenize-image', views.TokenizeImage.as_view(), name='tokenize-image'),
    path('temp', views.Temp.as_view(), name='temp')
]
