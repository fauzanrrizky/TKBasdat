from django.urls import path
from example_app.views import index

app_name = 'peminjaman_stadium'

urlpatterns = [
    path('', index, name='index'),
]