from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='Home-Page'),
    path('my_information', views.user_informations, name='User-Information'),
    path('login', views.login, name='Login'),
    path('create_account', views.create_account, name='Create-Account'),
]