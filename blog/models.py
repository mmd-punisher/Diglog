from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def posts_num(self):
        return Post.objects.filter(category=self.name).count()

    def get_absolute_url(self):
        return reverse('home-url')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField()
    # body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Daily')
    slug = models.SlugField(max_length=100, unique=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    short_description = models.CharField(max_length=300)
    date_updated = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail-url', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # Associate with User model
    bio = models.TextField(max_length=500)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('show-profile-url', kwargs={"slug": self.slug})
        return reverse('home-url')


class Comment(models.Model):
    # todo: Delete and Edit comments
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=355)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' - ' + str(self.post)
