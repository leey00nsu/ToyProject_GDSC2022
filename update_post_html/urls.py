from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.redirect_to_update, name='redirect'),
]