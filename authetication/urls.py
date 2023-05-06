from django.urls import path
from authentication.views import *

app_name = 'authetication'

urlpatterns = [
    path('', authentication, name='authentication'),
]