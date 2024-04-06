from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordChangingForm
from blog.models import Profile


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success-url')
    template_name = 'registration/change_password.html'


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home-url')

    def get_object(self):
        return self.request.user


class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowProfileView, self).get_context_data(**kwargs)
        the_user = get_object_or_404(Profile, slug=self.kwargs['slug'])
        context['the_user'] = the_user
        return context
