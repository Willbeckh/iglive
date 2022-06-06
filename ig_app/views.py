from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# app imports
from .forms import CreateUserForm
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

        def get(self, request):
            context = {
                'form': self.form
            }
            return render(request, 'ig_app/register.html', context)

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
