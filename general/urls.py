from django.urls import path

from general.views import index, logout, profile, admin_portal, add_order, admin_panel, confirm_order, cancel_order, \
    execute_order, delete_order, register_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin_portal/', admin_portal, name='admin_portal'),
    path('profile/', profile, name='profile'),
    path('add_order/', add_order, name='add_order'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('confirm_order/<int:order_id>/', confirm_order, name='confirm_order'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('execute_order/<int:order_id>/', execute_order, name='execute_order'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
    path('register_user/', register_user, name='register_user'),
]
