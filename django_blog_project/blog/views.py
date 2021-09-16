from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # <app>/<model>_<view>.html  is the default name which postListView.as_view() will look for. to change that, set
    # template_name
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):   # this will look for blog/post_detail.html template by default
    model = Post


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})



