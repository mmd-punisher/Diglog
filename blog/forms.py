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

    # header_image = forms.ImageField(label='Header Image', required=False,
    #                                 error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'short_description', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Title here'}),
            'author': forms.TextInput(
                attrs={'class': 'full-width', 'value': '', 'id': 'auther_field', 'type': 'hidden'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'full-width'}),
            'short_description': forms.Textarea(attrs={
                'class': 'full-width',
                'placeholder': 'Write a short description about your post, this text will showed up on main preview.',
                'rows': 3}),
            'body': forms.Textarea(attrs={'class': 'full-width', 'placeholder': 'Text here'}),
            # 'header_image': forms.ImageField(label='Header Image', required=False,
            #                                  error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
        }


class EditForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'category', 'short_description', 'body', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'full-width'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'full-width'}),
            'short_description': forms.Textarea(attrs={
                'class': 'full-width',
                'placeholder': 'Write a short description about your post, this text will showed up on main preview.',
                'rows': 3}),
            'body': forms.Textarea(attrs={'class': 'full-width'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            # 'name': forms.TextInput(
            #     attrs={'class': 'full-width', 'value': '', 'id': 'name_field', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'full-width'})
        }
