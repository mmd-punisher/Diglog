from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """
        def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        # Little changes here: {self.instance.pk} -> members
        if password:
            password.help_text = password.help_text.format(
                f"../../members/password/"
            )
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_login = forms.CharField(max_length=200,
                                 widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))
    # is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': "form-check"}))
    # is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': "form-check"}))
    # is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': "form-check"}))
    date_joined = forms.CharField(max_length=200,
                                  widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',
                  'last_login', 'date_joined']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=20,
                                   widget=forms.PasswordInput(attrs={'class': "form-control", 'type': 'password'}))
    new_password1 = forms.CharField(max_length=20,
                                    widget=forms.PasswordInput(attrs={'class': "form-control", 'type': 'password'}))
    new_password2 = forms.CharField(max_length=20,
                                    widget=forms.PasswordInput(attrs={'class': "form-control", 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_link', 'instagram_link', 'twitter_link']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_pic': forms,
            'website_link': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.TextInput(attrs={'class': 'form-control'})
        }
