from django.urls import path
from . import views
urlpatterns = [
    path('', views.profiles , name='profiles'),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logOutPage , name="logout"),
    path('register/', views.register , name="register"),
    path('userprofile/<str:pk>/', views.userProfile, name='userprofile'),
    path('account/',views.userAccount, name='account'),
    path('editaccount/',views.editAccount, name='editaccount'),
    path('create-skill/',views.createSkill, name='createskill'),
]