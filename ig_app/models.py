import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    profile_pic = models.ImageField(
        'profile photo', upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_bio(self):
        '''this method saves the user bio'''
        return self.save()

    def update_bio(self):
        '''this method updates the user bio'''
        return self.update()

    def delete_bio(self):
        '''this method deletes the user bio'''
        return self.delete()


class Post(models.Model):
    image_file = models.ImageField('post image', upload_to='images/')
    image_name = models.CharField('image name', max_length=50, blank=True)
    image_caption = models.TextField(max_length=500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(
        UserProfile, related_name='likes', blank=True)
    comments = models.ManyToManyField(
        UserProfile, related_name='comments', blank=True)

    def __str__(self):
        return self.image_name

    def was_published_recently(self):
        """this method checks if post was created recently
        Returns:
            True if post was created in the last 24 hours, otherwise False"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now


# todo: create posts model