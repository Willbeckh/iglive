"""this defines the urlconf of the ig application"""
from django.urls import path

#local imports
from ig_app.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index')
]