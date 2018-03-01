from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('g/<int:id>', views.group, name='group-detail'),
    path('events', views.events, name='events'),
    path('e/<int:id>', views.event, name='event')
]
