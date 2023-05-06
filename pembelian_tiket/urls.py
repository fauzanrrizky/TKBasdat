from django.urls import path
from example_app.views import index

app_name = 'pembelian_tiket'

urlpatterns = [
    path('', index, name='index'),
]