from django.shortcuts import render, redirect
from blog.models import Category


def index(request):
    # return render(request, 'landing/index_page.html')
    return redirect('home-url')


def header_component(request):
    categories_menu = Category.objects.all()
    all_cats = []
    for cat in categories_menu:
        all_cats.append(cat.name)
    context = {'categories_menu': all_cats}
    return render(request, 'header_partial.html', context)


def footer_component(request):
    return render(request, 'footer_partial.html')
