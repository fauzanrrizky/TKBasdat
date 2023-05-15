from django.urls import path
from mengelola_tim.views import *

app_name = 'mengelola_tim'

urlpatterns = [
    path('', mengelola_tim, name='mengelola_tim'),
    path('regist', regist, name='regist'),
]