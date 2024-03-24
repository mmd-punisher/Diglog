from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_url'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail_url')
]
