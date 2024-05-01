from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.forms import PostForm, EditForm, CommentForm
from blog.models import Post, Category, Comment
from hitcount.views import HitCountDetailView


def index(request):
    return render(request, 'blog/index.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        li = get_object_or_404(Post, slug=self.kwargs['slug'])
        total_likes = li.total_likes()
        liked = False
        if li.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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


def like_view(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_like'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)  # Not only we save the like, we also save the user
        liked = True

    return HttpResponseRedirect(reverse('post-detail-url', args=[str(slug)]))


# def user_profile(request, username):
#     the_user = Profile.objects.get(username=request.user.username)
#     return render()

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home-url')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_post = Post.objects.filter(title__icontains=searched)
        return render(request, 'search.html', {'searched': searched, 'posts': search_post})
    else:
        return render(request, 'search.html', {})
