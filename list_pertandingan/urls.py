from django.urls import path
from list_pertandingan.views import *

app_name = 'ist_pertandingan'

urlpatterns = [
    path('', list_pertandingan, name='list_pertandingan'),
]