from django.urls import path

from general.views import index, logout, profile, admin_portal, add_order, admin_panel
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin_portal/', admin_portal, name='admin_portal'),
    path('profile/', profile, name='profile'),
    path('add_order/', add_order, name='add_order'),
    path('admin_panel/', admin_panel, name='admin_panel'),
]