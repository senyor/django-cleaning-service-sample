from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404

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
    order_list_by_user = Order.objects.all().order_by('-date_at')
    context = {"order_list_by_user": order_list_by_user}
    return render(request, "admin_panel.html", context)


def confirm_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, pk=order_id)
        order.status = '1'
        order.save()
        return redirect('admin_panel')


def cancel_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == "POST":
        cancel_reason = request.POST.get('comment')
        order.comment = cancel_reason
        order.status = '3'
        order.save()
        return redirect('admin_panel')

    context = {"order": order}

    return render(request, "cancel_order.html", context)


def execute_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, pk=order_id)
        order.status = '2'
        order.save()
        return redirect('admin_panel')


def delete_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return redirect('admin_panel')


def admin_portal(request):
    return redirect('/admin')


def logout(request):
    auth.logout(request)
    return redirect('index')
