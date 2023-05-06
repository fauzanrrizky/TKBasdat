from django.urls import path
from example_app.views import index

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index'),
]