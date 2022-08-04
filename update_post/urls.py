from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_post, name='update_post'),
]