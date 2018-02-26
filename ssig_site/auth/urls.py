from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='auth'),
    path('callback', views.callback),
    path('logout', views.logout),
]
