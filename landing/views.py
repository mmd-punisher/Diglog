from django.shortcuts import render

from blog.models import Category


def index(request):
    return render(request, 'landing/index_page.html')


def header_component(request):
    categories_menu = Category.objects.all()
    all_cats = []
    for cat in categories_menu:
        all_cats.append(cat.name)
    context = {'categories_menu': all_cats}
    return render(request, 'landing/header_partial.html', context)


def footer_component(request):
    return render(request, 'landing/footer_partial.html')
