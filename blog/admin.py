from django.contrib import admin
from .models import Post, Category, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
