from dataclasses import field
from multiprocessing import context
from django.shortcuts import render
from contents/models.py import NewPost

def open_post(request, id):
    OpenPost = get_objsct_or_404(NewPost, pk=id)

    context = {
        'Post' : OpenPost
    }

    return render(request, 'templates/', context)
