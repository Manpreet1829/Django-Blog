from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Manpreet Kaur',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'September 1st,2021'
    },
    {
        'author': 'Manpreet Kaur',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'September 1st,2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
