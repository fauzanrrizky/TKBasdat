from django.urls import path
from mulai_pertandingan.views import *

app_name = 'mulai_pertandingan'

urlpatterns = [
    path('', mulai_pertandingan, name='mulai_pertandingan'),
]