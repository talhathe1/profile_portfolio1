from django.urls import path
from . import views


urlpatterns = [
    path('', views.members, name='home'),
    path('project-details/', views.project_details, name='details'),
    path('projects/', views.projects, name='projects'),
    path('specialization/', views.specialization, name='specialization'),

]
