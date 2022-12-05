
from django.urls import path

from .views import register_user_view

app_name = 'signup'


urlpatterns  = [
        path('', register_user_view, name='register_user_view'),

]