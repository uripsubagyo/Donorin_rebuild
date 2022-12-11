from django.conf.urls import url, include
from .views import login_flutter

app_name = 'authentication'

urlpatterns = [
    url('login/', login_flutter, name='login_flutter'),
    # url('signup_flutter/', signup_flutter, name='signup_flutter'),
    # url('logout_flutter/', logout_flutter, name='logout_flutter'),
]
