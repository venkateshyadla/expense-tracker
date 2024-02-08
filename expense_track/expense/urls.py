from django.urls import path
from .views import register,login,dashboard,add_expense,welcome,logout
urlpatterns = [
 # Add more paths for other views if needed
 path('',welcome,name='welcome'),
 path('register/',register,name='register'),
 path('login/',login,name = 'login'),
 path('dashboard/',dashboard,name='dashboard'),
 path('add_expense/',add_expense,name='add_expense'),
 path('logout/',logout,name='logout')
]  