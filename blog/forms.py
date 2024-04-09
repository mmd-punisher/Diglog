from django import forms
from .models import Post, Category, Comment
from ckeditor.widgets import CKEditorWidget
from .category_adder import display_choices


# choices = Category.objects.all().values_list('name', 'name')
# choices_list = []
# for choice in choices:
#     choices_list.append(choice)


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'short_description', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title here'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'auther_field', 'type': 'hidden'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short description about your post, this text will showed up on main preview.',
                'rows': 3}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text here'}),
        }


class EditForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'category', 'short_description', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short description about your post, this text will showed up on main preview.',
                'rows': 3}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
