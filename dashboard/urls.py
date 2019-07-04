from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserDashboard, name='dashboard'),
    path('/newproject', views.CreateProject, name='newproject'),
]
