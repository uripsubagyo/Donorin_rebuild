from django.conf.urls import url, include
from .views import login_flutter, signup_flutter, logout_flutter, get_user

app_name = 'authentication'

urlpatterns = [
    # url('login_flutter/', login_flutter, name='login_flutter'),
    # url('signup_flutter/', signup_flutter, name='signup_flutter'),
    # url('logout_flutter/', logout_flutter, name='logout_flutter'),
]
