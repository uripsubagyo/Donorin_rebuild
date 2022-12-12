from django.urls import path
from jadwal.views import *

app_name = 'jadwal'

urlpatterns = [
    path('', show_jadwal, name='show_jadwal'),
    path('delete/<int:id>', delete, name='delete'),
    path('book/', book_jadwal, name='book_jadwal'),
    path('location/', show_location, name='show_location'),
    path('show-jadwal-flutter/', show_jadwal_json, name='show_jadwal_json'),
    path('add-jadwal-flutter/', add_jadwal_flutter, name='add_jadwal_flutter'),
    path('delete-flutter/', delete_jadwal_flutter, name='delete_jadwal_flutter'),
    path('get-jadwal-user/', get_jadwal_user, name='get_jadwal_user'),
]