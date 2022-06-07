'''all the application forms live here'''
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# local apps
from ig_app.models import Post


# your code here
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username..'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        }
        
        
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image_file', 'image_name', 'image_caption']
        
        widgets = {
            'image_caption': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Image caption...', 'cols':30, 'rows':5}),
        }