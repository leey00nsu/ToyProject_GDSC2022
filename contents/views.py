import datetime
import re
from this import d
from django.shortcuts import get_object_or_404,render, redirect
from django.forms import ModelForm
from .models import NewPost
from accounts.models import *

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
        if (post.title == None):
            post.title = "제목없음"
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

def change_view_mode(request):
    view_mode = get_object_or_404(Profile, pk=request.user.id)
    view_mode_list = {'all', 'diary', 'memo'}
    for mode in view_mode_list:
        if (mode in request.POST):
            view_mode.view_mode = mode
            view_mode.save()
            return redirect('/')
