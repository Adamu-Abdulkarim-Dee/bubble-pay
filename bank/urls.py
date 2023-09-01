from django.urls import path
from . import views

urlpatterns = [
    path('bank', views.dashboard, name='Dashboard'), 
    path('transfer', views.transfer, name='Transfer'),
    path('history', views.history, name='History'),
    path('make_transfer', views.make_transfer, name='Make-Transfer'),
    path('transfer-to-other', views.transfer_to_other, name='Transfer-To-Other')
]