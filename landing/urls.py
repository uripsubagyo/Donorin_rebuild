from django.urls import path

from landing.views import showLanding, addNews, getAddNews

app_name = 'landing'

urlpatterns = [
    path('', showLanding, name='showLanding'),
    path('addNews/', addNews, name='addNews'),
    path('getAddNews', getAddNews, name='getAddNews')
]