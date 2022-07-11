from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):

        return render(request, 'contents/content.html')
        #return render(request, 'main_view/main_intro.html')