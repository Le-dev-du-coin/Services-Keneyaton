from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from store.models import Customer, Order, OrderItem
from django.contrib import messages


def signin(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                device = request.session['device']
                if device:
                    # Récupérez le panier associé à l'identifiant de session
                    (device_customer, created) = Customer.objects.get_or_create(device=device)
                    device_order, created = Order.objects.get_or_create(customer=device_customer, complete=False)

                    # Transférez les produits du panier de l'identifiant de session au panier de l'utilisateur
                    customer = request.user.customer
                    customer_order, created = Order.objects.get_or_create(customer=customer, complete=False)

                    # Transfert des produits
                    for order_item in device_order.orderitem_set.all():
                        order_item.order = user_order
                        order_item.save()

                    # Supprimez le panier de l'identifiant de session
                    device_order.delete()
                    if customer_order.orderitem_set.all().count() >= 1:
                        return redirect('panier')
                else:
                    return redirect('home')
        else:
            messages.error(request, "Email ou mot de passe incorrect !")
    return render(request, "authentication/login.html")


