from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPage, name='frontpage'),
    path('', views.FrontPage, name='home'),
]
