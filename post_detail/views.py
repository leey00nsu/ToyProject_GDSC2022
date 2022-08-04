from django.shortcuts import get_object_or_404, render
from contents.models import NewPost

def open_post(request, id):
    #OpenPost로 db에서 세부내용을 가져옴.
    OpenPost = get_object_or_404(NewPost, pk=id)
    
    #contents/content12312.html로 세부내용을 OpenPost라는 이름으로 보냄.
    return render(request, 'contents/content_view.html', {'OpenPost' : OpenPost})