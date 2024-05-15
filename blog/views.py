from collections import Counter

from django.contrib.auth import logout
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage
from blog.forms import PostForm, EditForm, CommentForm
from blog.models import Post, Category, Comment
from hitcount.views import HitCountDetailView


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu

        top_3_posts = Post.objects.all().order_by('-likes')[:3]
        page_num = self.request.GET.get('page', 1)

        if page_num == '1' or page_num == 1:
            main_posts = Post.objects.exclude(id__in=top_3_posts.values_list('id', flat=True)).order_by('-pub_date')
        else:
            main_posts = Post.objects.order_by('-pub_date')

        paginator = Paginator(main_posts, 10)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)

        context.update({
            'top_3_posts': top_3_posts,
            'page': page
        })

        return context


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        total_likes = post.total_likes()
        liked = post.likes.filter(id=self.request.user.id).exists()
        comment_form = CommentForm()

        context.update({
            'total_likes': total_likes,
            'liked': liked,
            'comment_form': comment_form,
            'comments': post.comment_set.all()
        })

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post  # Make sure to link the comment to the post
            new_comment.save()
            return redirect('post-detail-url', slug=post.slug)

        # If the form is not valid, re-render the detail view with form errors
        context = self.get_context_data()
        context['comment_form'] = comment_form
        return self.render_to_response(context)


"""    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        total_likes = post.total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comments = post.comment_set.all()
        new_comment = None
        if self.request.method == 'POST':
            comment_form = CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.author = self.request.user
                new_comment.save()
                return redirect('post-detail-url', slug=self.kwargs['slug'])
        else:
            comment_form = CommentForm()

        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'total_likes': total_likes,
            'liked': liked,
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        })

        return context
"""


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    # fields = ['title', 'author', 'body']


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_post.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home-url')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'


def category_list(request, category_name):
    category_post = Post.objects.filter(category__icontains=category_name.replace('-', ' ')).order_by('-pub_date')
    context = {'category_post': category_post, 'category_name': category_name.replace('-', ' ')}
    return render(request, 'blog/categories.html', context)


def category_menu(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    category_counts = Counter(post.category for post in posts)
    category_cats = [(category.name, category_counts[category.name]) for category in categories]

    context = {'categories_menu': category_cats}
    return render(request, 'blog/category_menu.html', context)


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


class AddCommentView(CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home-url')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_post = Post.objects.filter(title__icontains=searched).order_by('-pub_date')
        return render(request, 'blog/search.html', {'searched': searched, 'posts': search_post})
    else:
        return render(request, 'blog/search.html', {})


def about(request):
    return render(request, 'blog/about_us.html', {})
