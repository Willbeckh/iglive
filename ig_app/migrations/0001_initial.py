# Generated by Django 4.0.4 on 2022-06-06 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics/', verbose_name='profile photo')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images/', verbose_name='post image')),
                ('image_name', models.CharField(blank=True, max_length=50, verbose_name='image name')),
                ('image_caption', models.TextField(blank=True, max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ManyToManyField(blank=True, related_name='comments', to='ig_app.userprofile')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to='ig_app.userprofile')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
