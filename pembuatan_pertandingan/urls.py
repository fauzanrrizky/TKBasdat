from django.urls import path
from pembuatan_pertandingan.views import *

app_name = 'pembuatan_pertandingan'

urlpatterns = [
    path('', pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('lanjutan/', pembuatan_pertandingan_lanjutan, name='pembuatan_pertandingan_lanjutan'),
]