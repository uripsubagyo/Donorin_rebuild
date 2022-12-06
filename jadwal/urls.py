from django.urls import path
from .views import show_jadwal, delete, book_jadwal, show_location

app_name = 'jadwal'

urlpatterns = [
    path('', show_jadwal, name='show_jadwal'),
    path('delete/<int:id>', delete, name='delete'),
    path('book/', book_jadwal, name='book_jadwal'),
    path('location/', show_location, name='show_location'),
]