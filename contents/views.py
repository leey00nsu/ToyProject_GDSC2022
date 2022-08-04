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
        post.tag = request.POST['tag']
        try:
            if (post.imgfile != ''):
                post.imgfile = request.FILES['imgfile']
            else:
                post.imgfile = None
        except:
            post.imgfile = None
        
        post.save()
       
        
    return redirect('/')
    
        
