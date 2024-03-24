from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-url'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail-url'),
    path('create/', views.PostCreateView.as_view(), name='create-post-url')
]
