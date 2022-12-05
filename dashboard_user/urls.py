
from django.urls import path

from .views import dashboard_relawan

app_name = 'dashboard_user'

urlpatterns  = [
        path('', dashboard_relawan, name='dashboard_relawan'),
        
]
