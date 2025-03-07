from django.contrib import auth
from django.shortcuts import render, redirect

from general.models import Order


def index(request):
    return render(request, "index.html")


def profile(request):
    user = request.user
    if not user.is_authenticated or user.is_superuser:
        return redirect('index')

    order_list_by_user = Order.objects.filter(user=user).order_by('-date_at')
    context = {"order_list_by_user": order_list_by_user}
    return render(request, "profile.html", context)

def add_order(request):
    user = request.user
    if not user.is_authenticated or user.is_superuser:
        return redirect('index')

    return render(request, "add_order.html")

def admin_panel(request):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return redirect('index')

    return render(request, "admin_panel.html")


def admin_portal(request):
    return redirect('/admin')


def logout(request):
    auth.logout(request)
    return redirect('index')
