import datetime
from contents.models import NewPost
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def update_post(request, id):
    
    if request.method == 'POST':
        
        post = get_object_or_404(NewPost, pk=id)
        post.last_modified = datetime.datetime.now()
        
        post.title = request.POST['title']
        post.content = request.POST['body']
        
        if (request.FILES['imgfile'] != ''):
            post.imgfile = request.FILES['imgfile']
        
        post.save()
       
        
    return redirect('/')