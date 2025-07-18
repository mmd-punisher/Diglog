from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "full-width"}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "full-width"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "full-width"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'full-width'
        self.fields['password1'].widget.attrs['class'] = 'full-width'
        self.fields['password2'].widget.attrs['class'] = 'full-width'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "full-width"}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "full-width"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "full-width"}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "full-width"}))
    last_login = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class': "full-width", 'readonly': 'readonly'}))
    date_joined = forms.CharField(max_length=200,
                                  widget=forms.TextInput(attrs={'class': "full-width", 'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',
                  'last_login', 'date_joined']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=20,
                                   widget=forms.PasswordInput(attrs={'class': "full-width", 'type': 'password'}))
    new_password1 = forms.CharField(max_length=20,
                                    widget=forms.PasswordInput(attrs={'class': "full-width", 'type': 'password'}))
    new_password2 = forms.CharField(max_length=20,
                                    widget=forms.PasswordInput(attrs={'class': "full-width", 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_link', 'instagram_link', 'twitter_link']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'full-width', 'placeholder': 'Maximum 500 characters'}),
            # 'profile_pic': forms,
            'website_link': forms.TextInput(attrs={'class': 'full-width'}),
            'instagram_link': forms.TextInput(attrs={'class': 'full-width'}),
            'twitter_link': forms.TextInput(attrs={'class': 'full-width'})
        }
