from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.start, name='login'),
    path('callback', views.callback),
    path('logout', views.logout, name='logout'),
    path('password', auth_views.LoginView.as_view(template_name='password.html'), name='password')
]
