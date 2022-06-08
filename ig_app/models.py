import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
    image_file = CloudinaryField('post image')
    image_name = models.CharField('image name', max_length=50, blank=True)
    image_caption = models.TextField(max_length=500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True, default=None)
    comments = models.ManyToManyField(
        UserProfile, related_name='comments', blank=True)

    def __str__(self):
        return self.image_caption[:16]

    def was_published_recently(self):
        """this method checks if post was created recently
        Returns:
            True if post was created in the last 24 hours, otherwise False"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now

    def save_post(self):
        '''this method saves the post'''
        return self.save()

    def update_post(self):
        '''this method updates the post'''
        return self.update()

    def delete_post(self):
        '''this method deletes the post'''
        return self.delete()

    @property
    def total_likes(self):
        '''this method returns the total number of likes'''
        return self.likes.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


# todo: create likes model
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return self.user.username

    def save_like(self):
        '''this method saves the like'''
        return self.save()

    def update_like(self):
        '''this method updates the like'''
        return self.update()

    def delete_like(self):
        '''this method deletes the like'''
        return self.delete()
