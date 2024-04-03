from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-url'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile-url'),

]
