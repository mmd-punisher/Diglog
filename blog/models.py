from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('post-detail-url', args=(str(self.id)))
        return reverse('home-url')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Daily')
    slug = models.SlugField(max_length=100, unique=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    short_description = models.CharField(max_length=350)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail-url', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
