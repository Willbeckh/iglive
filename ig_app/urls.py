"""this defines the urlconf of the ig application"""
from django.urls import path
# from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required, permission_required

# local imports
from ig_app.views import HomeView, RegisterView, LoginView, LogoutView, PostView, ProfileView, LikeView

app_name = 'igapp'  # application namespace
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('newpost/', PostView.as_view(), name='newpost'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('like/', LikeView.as_view(), name='like'),
]
