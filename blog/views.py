from collections import Counter

from django.contrib.auth import logout
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage
from blog.forms import PostForm, EditForm, CommentForm
from blog.models import Post, Category, Comment, Profile
from hitcount.views import HitCountDetailView


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
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


"""
SECOND LOGIC

        page_num = self.request.GET.get('page', 1)
        if page_num == '1':
            main_posts = Post.objects.exclude(id__in=top_3_posts.values_list('id', flat=True)).order_by('-pub_date')
        else:
            main_posts = Post.objects.order_by('-pub_date')

        paginator = Paginator(main_posts, 4)  # Show 10 posts per page
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)
        print(page.object_list)
        print(Post.objects.all().order_by('-pub_date'))
        context.update({
            'top_3_posts': top_3_posts,
            'page': page
        })

"""

"""        top_posts = Post.objects.all().order_by('-likes')[:3]
        excluded_ids = [post.id for post in top_posts]
        other_posts = Post.objects.exclude(id__in=excluded_ids).order_by('-pub_date')

        # Set up pagination
        paginator = Paginator(other_posts, 5)  # Adjust the number to display per page as needed
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        print(top_posts)
        print(other_posts)
        context.update({
            'top_posts': top_posts,
            'page_obj': page_obj}
        )"""

"""     OLD LOGIC
        # 3 top posts
        top_3posts = Post.objects.all().order_by('-likes')[:3]

        # Paging
        staff = Post.objects.order_by('-pub_date')
        p = Paginator(staff, 10)
        page_num = self.request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        if page.number == 1:
            page = p.page(page_num)
            print(page.object_list)

        context.update({
            'top_3posts': top_3posts,
            'page': page,
        })"""


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

        # user_request = self.request.user
        # current_user = Profile.objects.get(slug=user_request.username)

        context["total_likes"] = total_likes
        context["liked"] = liked
        # context["current_user"] = current_user
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
    categories = Category.objects.all()
    posts = Post.objects.all()
    category_counts = Counter(post.category for post in posts)
    category_cats = [(category.name, category_counts[category.name]) for category in categories]

    context = {'categories_menu': category_cats}
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
        search_post = Post.objects.filter(title__icontains=searched).order_by('-pub_date')
        return render(request, 'search.html', {'searched': searched, 'posts': search_post})
    else:
        return render(request, 'search.html', {})


def about(request):
    return render(request, 'about_us.html', {})
