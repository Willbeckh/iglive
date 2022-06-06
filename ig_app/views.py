from ast import Return
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm

# app imports
from .forms import CreateUserForm

# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Home',
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
                form = CreateUserForm() # reset the form
                
            context = {
                'form': form
            }
            return render(request, 'ig_app/register.html', context)
    except Exception as e:
        raise Http404('form validation error occured',e)