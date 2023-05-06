from django.urls import path
from example_app.views import index

app_name = 'history_rapat'

urlpatterns = [
    path('', index, name='index'),
]