from django.contrib import admin

# local imports
from ig_app.models import Post, UserProfile
 
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['image_name']}),
        ('Caption', {'fields': ['image_caption']}),
        ('Image', {'fields': ['image_file']}),
    ]
    
admin.site.register(Post, PostAdmin)