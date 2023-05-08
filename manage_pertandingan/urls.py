from django.urls import path
from manage_pertandingan.views import *

app_name = 'manage_pertandingan'

urlpatterns = [
    path('', manage_pertandingan, name='manage_pertandingan'),
    path('peristiwa/', peristiwa , name='peristiwa'),
    path('buat_pertandingan/', buat_pertandingan , name='buat_pertandingan'),
    path('akhir_musim/', akhir_musim , name='akhir_musim'),
]