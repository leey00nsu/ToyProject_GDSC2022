import datetime
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import NewPost

# Create your views here.
def post_new(request):
    
    if request.method == 'POST':
        
        post = NewPost()
        
        post.date = datetime.datetime.now()
        post.title = request.POST['title']
        post.content = request.POST['body']
        
        post.save()
    elif request.method == 'GET':
        return render(request, 'contents/content.html')
    
        
    return render(request, 'contents/content.html')
    
        
