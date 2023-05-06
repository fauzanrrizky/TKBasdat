from django.urls import path
from example_app.views import index

app_name = 'mulai_rapat'

urlpatterns = [
    path('', index, name='index'),
]