from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# app imports
from .forms import CreateUserForm, CreatePostForm
from .models import Post


# Create your views here.
class HomeView(View):
    def get(self, request):
        posts = Post.objects.order_by('-pub_date')[:20]
        context = {
            'title': 'Home',
            'posts': posts
        }
        return render(request, 'ig_app/index.html', context)


# register view class
class RegisterView(View):
    '''this class handles the register form page and user creation process'''
    try:
        form = CreateUserForm()
        context = {
            'form': form
        }

        def get(self, request):
            return render(request, 'ig_app/register.html', self.context)

        def post(self, request):
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                form = CreateUserForm()  # reset the form
                messages.success(request, 'Account registered successfully!')
                return redirect(reverse('igapp:login'))
            context = {
                'form': form
            }
            return render(request, 'ig_app/register.html', context)
    except Exception as e:
        raise Http404('form validation error occured', e)


class LoginView(View):
    context = {
        'title': 'Login',
    }

    def get(self, request):
        return render(request, 'ig_app/login.html', self.context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('igapp:index')
        else:
            messages.error(
                request, 'Invalid credentials, please provide valid credentials')
        return render(request, 'ig_app/login.html', self.context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('igapp:index')


# add post view
class PostView(View):
    form = CreatePostForm()
    context = {
        'title': 'New Post',
        'form': form
    }

    def get(self, request):
        return render(request, 'ig_app/post_form.html', self.context)

    # add post
    def post(self, request):
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form = CreatePostForm()
            messages.success(request, 'Post added successfully!')
            return redirect('igapp:index')
        context = {
            'form': form
        }
        return render(request, 'ig_app/post_form.html', context)
