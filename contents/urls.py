from django.urls import path
from .views import *

app_name = 'contents'

urlpatterns = [
    path('', post_new, name='post_new'),
    path('post_update/', post_update, name='post_update'),
]