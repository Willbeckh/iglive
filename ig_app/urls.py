"""this defines the urlconf of the ig application"""
from django.urls import path

# local imports
from ig_app.views import HomeView, RegisterView, LoginView

app_name = 'igapp'  # application namespace
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
