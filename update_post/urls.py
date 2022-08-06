from django.urls import path
from .views import *

app_name = 'update_post'

urlpatterns = [
    path('', update_post, name='update_post'),
]