from django.urls import path
from .views import index, select

urlpatterns = [
    path('', index, name='index'),
    path('select/', select, name='select'),
]