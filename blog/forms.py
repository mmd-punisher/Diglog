from django import forms
from .models import Post, Category
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
        fields = ['title', 'author', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text here'}),
        }


class EditForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=display_choices(), attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
