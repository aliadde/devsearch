from django.urls import path
from . import views



urlpatterns = [
    path('', views.base, name='base'),
    path('single/', views.singlepage, name='singleproject'),
    path('projects/', views.projects, name='projects'),
    
]
