import datetime
import re
from this import d
from django.shortcuts import get_object_or_404,render, redirect
from django.forms import ModelForm
from .models import NewPost

# Create your views here.
def post_new(request):
    
    if request.method == 'POST':
        
        
        post = NewPost()
        post.user = request.user.username
        post.date = datetime.datetime.now()
        post.last_modified = post.date
        post.title = request.POST['title']
        post.content = request.POST['content']
        	

        
        
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
    
        
def post_update(request):

    if request.method == 'POST':
        post = get_object_or_404(NewPost, pk=request.POST['post_num'])
        print(post.tag)
        
        post.last_modified = datetime.datetime.now()
        post.title = request.POST['title']
        post.content = request.POST['content']
        	
        post.tag = request.POST.get('tag','메모')
        
        
        try:
            if (request.FILES['imgfile'] != ''):
                post.imgfile = request.FILES['imgfile']
            else:
                post.imgfile = None
        except:
            post.imgfile = None
        
        post.save()
       
        
    return redirect('/')