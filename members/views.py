from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from blog.models import Profile
from .forms import RegisterForm, EditProfileForm, PasswordChangingForm, ProfilePageForm


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
    template_name = 'registration/edit_settings.html'
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


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_link', 'instagram_link', 'twitter_link']
    success_url = reverse_lazy('home-url')


class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProfilePageView, self).form_valid(form)
