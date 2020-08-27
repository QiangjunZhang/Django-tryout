from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.account_login, name='login'),
    path('loginout/', views.account_login_out, name='loginOut'),
]