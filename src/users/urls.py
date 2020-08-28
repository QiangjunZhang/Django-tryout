from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.account_login, name='login'),
    path('update/', views.update_profile, name='update'),
    path('loginout/', views.account_login_out, name='loginOut'),



]