from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User,related_name='account', default=None,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    Heading=models.CharField(max_length=200)
    SubHeading = models.CharField(max_length=200, null=True)
    Thumb = models.ImageField(default='post-bg.jpg', blank=True)
    Content = RichTextField(blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post',blank=True)

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.Heading
    def snippet(self):
        return self.Content[:100]+'...'

class Comment(models.Model):
    user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.body
