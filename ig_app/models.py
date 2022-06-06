import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    profile_pic = models.ImageField('profile photo', upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.bio

