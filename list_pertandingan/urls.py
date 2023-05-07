from django.urls import path
from list_pertandingan.views import *

app_name = 'list_pertandingan'

urlpatterns = [
    path('', list_pertandingan, name='list_pertandingan'),
    path('penonton/', list_pertandingan_penonton, name='list_pertandingan_penonton'),
    path('manajer/', list_pertandingan_manajer, name='list_pertandingan_manajer'),
]