from django.contrib import admin
from django.urls import path, include
from app1 import views
urlpatterns = [
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]