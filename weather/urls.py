from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index.as_view(), name="index"),
    path('location/', views.WeatherStats.as_view(), name="location-stats"),
]