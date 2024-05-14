from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register-url'),
    path('edit-settings/', views.UserEditView.as_view(), name='edit-settings-url'),
    # path('password/', auth_views.PasswordChangeView.as_view(), name='password-change-url')
    path('password/', views.PasswordsChangeView.as_view(), name='password-change-view-url'),
    path('password-success/', views.password_success, name='password-success-url'),
    path('<slug:slug>/profile/', views.ShowProfileView.as_view(), name='show-profile-url'),
    path('<slug:slug>/edit-profile-page/', views.EditProfilePageView.as_view(), name='edit-profile-page-url'),
    path('create-profile-page/', views.CreateProfilePageView.as_view(), name='create-profile-page-url'),
]
