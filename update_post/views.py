import datetime
from contents.models import *
from django.shortcuts import render, get_object_or_404, redirect
import logging

# Create your views here.
def update_post(request):
    
    if request.method == 'POST':
        
        post = get_object_or_404(NewPost, pk=int(request.POST['id']))
        post.last_modified = datetime.datetime.now()
        
        post.title = request.POST['title']
        post.content = request.POST['body']

        if (request.FILES.get('imgfile') != ''):
            post.imgfile = request.FILES.get('imgfile')
        
        post.save()
       
        
        return redirect('../post_detail/'+request.POST['id']+'/', {'OpenPost' : post})
    
    
    else:
        return redirect('/')