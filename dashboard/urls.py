from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard_manajer/', dashboard_manajer, name='dashboard_manajer'),
    path('dashboard_panitia/', dashboard_panitia, name='dashboard_panitia'),
    path('dashboard_penonton/', dashboard_penonton, name='dashboard_penonton'),
]