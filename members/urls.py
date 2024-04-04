from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, password_success


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-url'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile-url'),
    # path('password/', auth_views.PasswordChangeView.as_view(), name='password-change-url')
    path('password/', PasswordsChangeView.as_view(), name='password-change-view-url'),
    path('password-success/', password_success, name='password-success-url')
]
