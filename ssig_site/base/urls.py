from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events', views.events, name='events'),
    path('events/<str:filter>/<str:time>', views.events, name='events'),

    path('e/<int:id>', views.event, name='event'),
    path('e/<int:id>/register', views.event_register, name='event-register'),
    path('e/<int:id>/unregister', views.event_unregister, name='event-unregister'),
    path('e/<int:id>/edit', views.event_edit, name='event-edit'),
    path('e/<int:id>/delete', views.event_delete, name='event-delete'),
    path('e/<int:id>/attendance', views.event_attendance, name='event-attendance'),

    path('g/<int:id>', views.group, name='group-detail'),
    path('g/<int:id>/join', views.group_join, name='group-join'),
    path('g/<int:id>/leave', views.group_leave, name='group-leave'),
    path('g/<int:id>/create-event', views.create_event, name='create-event'),

    path('tickets', views.tickets, name='tickets'),
    path('ticket/<int:id>', views.ticket, name='ticket'),
]
