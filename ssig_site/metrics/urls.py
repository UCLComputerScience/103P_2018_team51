from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='metrics-dashboard'),
    path('data/<str:name>/<str:period>.json', views.data),
]
