from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from contents.models import NewPost

@login_required
def open_post(request, id):
    #OpenPost로 db에서 세부내용을 가져옴.
    post = get_object_or_404(NewPost, pk=id)
    
    #contents/content12312.html로 세부내용을 OpenPost라는 이름으로 보냄.
    return render(request, 'contents/content_view.html', {'post' : post})

@login_required
def post_update(request, id):
    #OpenPost로 db에서 세부내용을 가져옴.
    post = get_object_or_404(NewPost, pk=id)
    
    #contents/content12312.html로 세부내용을 OpenPost라는 이름으로 보냄.
    return render(request, 'contents/content_update.html', {'post' : post})

@login_required
def post_delete(request,id):
    
    Post = get_object_or_404(NewPost, pk=id)
    if Post.user == request.user.username:
      Post.delete()
    return redirect("/")