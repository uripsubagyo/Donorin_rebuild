from django.urls import path

from landing.views import showLanding

app_name = 'landing'

urlpatterns = [
    path('', showLanding, name='showLanding'),
]