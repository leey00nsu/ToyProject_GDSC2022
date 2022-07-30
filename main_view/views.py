from django.shortcuts import render
from rest_framework.views import APIView
import datetime


class Main(APIView):
    def get(self, request):
      cur_user = request.user
      now = datetime.datetime.now().strftime('%Y년%m월%d일 %H시%M분')
      # 로그인한 유저인 경우
      if cur_user.is_authenticated:
        return render(request, 'contents/content.html',{'now':now})
      else:
      # 로그인 하지 않은 유저인 경우
        return render(request, 'main_view/main_intro.html')
