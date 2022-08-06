import datetime
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import NewPost

# Create your views here.
def post_new(request):
    
    if request.method == 'POST':
        
        print(request.POST)
        
        post = NewPost()
        post.user = request.user.username
        post.date = datetime.datetime.now()
        post.last_modified = post.date
        post.title = request.POST['title']
        post.content = request.POST['body']
        
        
        if (request.POST['tag'] == '1'):
            post.tag = '일기'
        elif (request.POST['tag'] == '2'):
            post.tag = '메모'
        
        
        try:
            if (request.FILES['imgfile'] != ''):
                post.imgfile = request.FILES['imgfile']
            else:
                post.imgfile = None
        except:
            post.imgfile = None
        
        post.save()
       
        
    return redirect('/')
    
        
