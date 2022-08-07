
from django.shortcuts import render
from rest_framework.views import APIView
from contents.models import NewPost
from django.db.models import Q
import datetime


class Main(APIView):
    def get(self, request):
      cur_user = request.user
      now = datetime.datetime.now().strftime('%Y년%m월%d일 %H시%M분')
      
      # PostList = NewPost.objects.filter(Q(user = request.user.username) & Q(tag=tags))
      PostList = NewPost.objects.filter(Q(user = request.user.username) )
      PostList = PostList.order_by('-date')
      
      # 로그인한 유저인 경우
      if cur_user.is_authenticated:
        return render(request, 'contents/content.html',{'now':now,'PostList' : PostList})
      else:
      # 로그인 하지 않은 유저인 경우
        return render(request, 'main_view/main_intro.html')
