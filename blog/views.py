from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import PostForm, EditForm
from blog.models import Post, Category


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']


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


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home-url')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def category_list(request, category_name):
    category_post = Post.objects.filter(category__icontains=category_name.replace('-', ' ')).order_by('-pub_date')
    context = {'category_post': category_post, 'category_name': category_name.replace('-', ' ')}
    return render(request, 'categories.html', context)


def category_menu(request):
    categories_menu = Category.objects.all()
    context = {'categories_menu': categories_menu}
    return render(request, 'category_menu.html', context)


def logout_view(request):
    logout(request)
    return redirect('home-url')
