from django.urls import path
from open_post import views

urlpatterns = [
    path('<int:question_id>/', views.open_post, name='open_post'),
]