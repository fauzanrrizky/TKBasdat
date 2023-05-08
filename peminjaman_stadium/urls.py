from django.urls import path
from peminjaman_stadium.views import *

app_name = 'peminjaman_stadium'

urlpatterns = [
    path('', peminjaman_stadium, name='peminjaman_stadium'),
    path('list_waktu/', list_waktu , name='list_waktu'),
]