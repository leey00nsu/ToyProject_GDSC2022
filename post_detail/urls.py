from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.open_post, name='open_post'),
    path('<int:id>/post_delete/',views.post_delete,name="post_delete"),
    path('<int:id>/post_update/',views.post_update,name="post_update"),
]
#포스트 내용을 보기위한 링크는 https://기본적 주소/post_detail/id(1이나 2 ... 몇번째 게시문인지 표시)/