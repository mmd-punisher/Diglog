from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Category, Profile, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category')
    prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
