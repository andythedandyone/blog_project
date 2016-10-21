from django.shortcuts import render
from .models import blogPost


def listPost(request):
    #
    # name = blogPost.objects.all()
    #
    # context = {'title' : name.title}


    return render(request, 'blog/main.html')


def newPost(request):
    pass


def editPost(request):
    pass


def deletePost(request):
    pass






