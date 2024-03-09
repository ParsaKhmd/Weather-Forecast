from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('weather/', views.get_weather_data, name='weather_page')
]
