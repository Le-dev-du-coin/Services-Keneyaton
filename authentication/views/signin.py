from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from store.models import Customer, Order, OrderItem
from django.contrib import messages


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                if "device" in request.session:
                    device = request.session["device"]
                    device_order, created = Order.objects.get_or_create(
                        customer=device, complete=False
                    )
                    if device_order.orderitem_set.all().count() > 0:
                        pass
        else:
            messages.error(request, "Email ou mot de passe incorrect !")

    return render(request, "authentication/login.html")
