from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import PostForm, EditForm
from blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    # fields = ['title', 'author', 'body']


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
