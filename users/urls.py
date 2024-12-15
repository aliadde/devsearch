from django.urls import path
from . import views
urlpatterns = [
    path('', views.profiles , name='profiles'),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logOutPage , name="logout"),
    path('register/', views.register , name="register"),
    path('user-profile/<str:pk>/', views.userprofile, name='user-profile'),
    path('user-profile/<str:pk>/', views.userprofile, name='user-profile'),
    path('account',views.userAccount, name='account'),
]