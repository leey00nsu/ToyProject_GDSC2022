from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.open_post, name='open_post'),
]
#포스트 내용을 보기위한 링크는 https://기본적 주소/post_detail/id(1이나 2 ... 몇번째 게시문인지 표시)/