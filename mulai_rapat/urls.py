from django.urls import path
from mulai_rapat.views import *

app_name = 'mulai_rapat'

urlpatterns = [
    path('', mulai_rapat, name='mulai_rapat'),
    path('rapat/', rapat_pertandingan, name='rapat_pertandingan'),
]