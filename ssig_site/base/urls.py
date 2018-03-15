from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events', views.events, name='events'),
    path('e/<int:id>', views.event, name='event'),
    path('e/<int:id>/register', views.event_register, name='event-register'),
    path('e/<int:id>/unregister', views.event_unregister, name='event-unregister'),

    path('g/<int:id>', views.group, name='group-detail'),
    path('g/<int:id>/join', views.group_join, name='group-join'),
    path('g/<int:id>/leave', views.group_leave, name='group-leave')
]
