from django.contrib import admin

# local imports
from ig_app.models import Post, UserProfile, Like

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['image_name']}),
        ('author', {'fields': ['user']}),
        ('Caption', {'fields': ['image_caption']}),
        ('Image', {'fields': ['image_file']}),
        ('Like', {'fields': ['likes']}),

    ]


admin.site.register(Post, PostAdmin)
