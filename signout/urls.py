
from django.urls import path
from .views import logout

app_name = 'signout'


urlpatterns  = [
        path('', logout, name='logout')
]