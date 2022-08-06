from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from contents.models import NewPost

# Create your views here.
def redirect_to_update(request, id):
    
    OpenPost = get_object_or_404(NewPost, pk=id)
       
    return render(request, 'contents/contents_update.html', {'OpenPost' : OpenPost, 'id' : id})