from django.shortcuts import render
from .models import blogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger











def listPost(request):

    query_result = blogPost.objects.all().order_by('-date_posted')

    paginator = Paginator(query_result, 6)



    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        result = paginator.page(paginator.num_pages)


    context = {'object_list' : result}









    return render(request, 'blog/main.html', context)










def view_post(request, id):

    query_post = blogPost.objects.filter(id=id)
    context = {'object_list' : query_post}

    return render(request, 'blog/fullpost.html', context)



def newPost(request):
    pass


def editPost(request):
    pass


def deletePost(request):
    pass




