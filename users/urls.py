from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logOutPage , name="logout"),
    path('', views.profiles , name='profiles'),
    path('user-profile/<str:pk>/', views.userprofile, name='user-profile'),
]