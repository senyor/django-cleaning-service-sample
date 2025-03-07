from django.urls import path

from general.views import index, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]