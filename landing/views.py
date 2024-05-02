from django.shortcuts import render


def index(request):
    return render(request, 'landing/index_page.html')


def header_component(request):
    return render(request, 'landing/header_partial.html')


def footer_component(request):
    return render(request, 'landing/footer_partial.html')
