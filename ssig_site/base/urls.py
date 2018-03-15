from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events', views.events, name='events'),
    path('e/<int:id>', views.event, name='event'),
    path('e/<int:id>/join', views.event_join, name='event-join'),
    path('e/<int:id>/leave', views.event_leave, name='event-leave'),

    path('g/<int:id>', views.group, name='group-detail'),
    path('g/<int:id>/join', views.group_join, name='group-join'),
    path('g/<int:id>/leave', views.group_leave, name='group-leave')
]
