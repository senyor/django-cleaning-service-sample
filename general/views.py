from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from general.forms import UserRegisterForm, OrderFillForm
from general.models import Order, UserProfile


def index(request):
    return render(request, "index.html")


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            fio = request.POST.get('fio')
            phone = request.POST.get('phone')
            user_profile = UserProfile.objects.create(user=user, fio=fio, phone=phone)
            user_profile.save()

            login(request, user)
            return redirect('index')

    context = {"form": form}
    return render(request, "register_user.html", context)


def profile(request):
    user = request.user
    if not user.is_authenticated or user.is_superuser:
        return redirect('index')
    order_list_by_user = Order.objects.filter(user=user).order_by('-date_at')
    context = {"order_list_by_user": order_list_by_user}
    return render(request, "profile.html", context)


def add_order(request):
    if not request.user.is_authenticated or request.user.is_superuser:
        return redirect('index')

    form = OrderFillForm()

    if request.method == "POST":
        checkbox = request.POST.get('checkbox', None)
        description = request.POST.get('description', None)
        order_type = request.POST.get('type', None)

        data_post = request.POST.copy()
        form = OrderFillForm(data_post)

        if checkbox:
            if not description:
                form.add_error('description', 'Укажите описание иной услуги')
            data_post['type'] = ''
        else:
            if not order_type:
                form.add_error('type', 'Укажите тип услуги')
            data_post['description'] = ''

    if form.is_valid():
        order = form.save(commit=False)
        order.user = request.user
        order.save()
        return redirect('profile')

    context = {"form": form}
    return render(request, "add_order.html", context )


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
