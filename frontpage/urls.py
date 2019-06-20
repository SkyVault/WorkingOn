from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPage, name='frontpage'),
    path('projects/<int:project_id>', views.ProjectView),
    path('', views.FrontPage, name='home'),
]
