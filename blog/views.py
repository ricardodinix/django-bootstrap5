from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.get(pk=1)
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
