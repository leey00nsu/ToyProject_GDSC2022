from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
      cur_user = request.user
      # 로그인한 유저인 경우
      if cur_user.is_authenticated:
        return render(request, 'contents/content.html')
      else:
      # 로그인 하지 않은 유저인 경우
        return render(request, 'main_view/main_intro.html')