# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post



def post_list(request):
       qs= Post.objects.all()
       return render(request, 'blog/post_list.html', {'post_list': qs,})


def post_detail(request,pk):

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post,})

