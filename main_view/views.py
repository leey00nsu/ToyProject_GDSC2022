
from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.views import APIView
from contents.models import NewPost
from accounts.models import Profile
from django.db.models import Q
from django.contrib.auth import get_user_model
import datetime


class Main(APIView):
    def get(self, request):
      now = datetime.datetime.now()
      # 리스트를 받아옵니다
      PostList = get_list(request,request.user)
      # 로그인한 유저인 경우
      if request.user.is_authenticated:
        return render(request, 'contents/content.html',{'now':now,'PostList' : PostList,'nickname':request.user.profile.nickname})
      else:
      # 로그인 하지 않은 유저인 경우
        return render(request, 'main_view/main_intro.html')

    def post(self, request):
      now = datetime.datetime.now()

      if request.method == 'POST':
        name = request.POST['search']
        print(name)
        if (name == ""):
          return redirect('/')
        else:
          PostList = get_list(request,name)
          print(PostList)
          if(PostList == None):
            return render(request, 'main_view/error404.html')
      else:
        PostList = get_list(request,request.user)
        
      # 로그인한 유저인 경우
      if request.user.is_authenticated:
        return render(request, 'contents/content_other.html',{'now':now,'PostList' : PostList,'nickname':name})
      else:
      # 로그인 하지 않은 유저인 경우
        return render(request, 'main_view/main_intro.html')

# 리스트 반환
    
def get_list(request,name):
    if not (name == request.user):
      is_user = Profile.objects.filter(nickname=name)
      if not(is_user):
        return 
        
      is_user = Profile.objects.filter(nickname=name)
      PostList = NewPost.objects.filter(Q(user = is_user[0].user) )
    else :
      PostList = NewPost.objects.filter(Q(user = request.user) )

    PostList = PostList.order_by('-date')
    return PostList
