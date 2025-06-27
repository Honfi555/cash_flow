"""URL-маршруты для приложения accounts."""

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

app_name = 'accounts'

urlpatterns = [
	path('', RedirectView.as_view(pattern_name='accounts:login', permanent=False)),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.RegisterView.as_view(), name='register'),
]
