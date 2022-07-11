from django.urls import path
from . import views
from . views import homepage

app_name='songs'

urlpatterns = [
    path('',homepage,name='home_page'),
]