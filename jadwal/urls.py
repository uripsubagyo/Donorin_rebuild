from django.urls import path
from jadwal.views import *

app_name = 'jadwal'

urlpatterns = [
    path('', show_jadwal, name='show_jadwal'),
    path('delete/<int:id>', delete, name='delete'),
    path('book/', book_jadwal, name='book_jadwal'),
    path('location/', show_location, name='show_location'),
]