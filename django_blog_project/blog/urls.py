from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

#<app>/<model>_<view>.html  is the default name which postListView.as_view() will look for.
