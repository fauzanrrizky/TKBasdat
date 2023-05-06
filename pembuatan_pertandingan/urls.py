from django.urls import path
from example_app.views import index

app_name = 'pembuatan_pertandingan'

urlpatterns = [
    path('', index, name='index'),
]