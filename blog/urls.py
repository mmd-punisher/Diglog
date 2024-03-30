from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-url'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail-url'),
    path('create/', views.PostCreateView.as_view(), name='create-post-url'),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name='edit-post-url'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-post-url'),
    path('add-category', views.AddCategoryView.as_view(), name='add-category-url'),
    path('category/<str:category_name>/', views.category_list, name='category-list-url'),
    path('categories/', views.category_menu, name='category-menu-url'),
    path('accounts/logout/', views.logout_view, name='logout-url'),

]
