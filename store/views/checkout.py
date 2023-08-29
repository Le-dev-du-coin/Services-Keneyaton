from django.shortcuts import render, redirect
from store.models import Order, OrderItem, ShippingAddress
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Email importation
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Checkout view
@login_required(login_url="register")
def checkout(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        if "device" in request.session:
            device = request.session["device"]
            customer = Customer.objects.get_or_create(customer=device)
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False
            )
            items = order.orderitem_set.all()
    context = {"items": items, "order": order}
    context = {"items": items, "order": order}
    return render(request, "store/payement.html", context)


# Process to payement
@login_required(login_url="login")
def processOrder(request):
    data = json(request.body)
    print(data)
    transaction_id = datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        first_name = data["shippingformData"]["fist_name"]
        last_name = data["shippingformData"]["last_name"]
        email = data["shippingformData"]["last_name"]
        phone_number = data["shippingformData"]["last_name"]
        country = data["shippingformData"]["last_name"]
        city = data["shippingformData"]["last_name"]
        street = data["shippingformData"]["last_name"]
        door = data["shippingformData"]["last_name"]
        door = data["shippingformData"]["last_name"]
        compagnie = data["shippingformData"]["last_name"]
        payement = data["shippingformData"]["last_name"]

        total = data["shippingformData"]["total"]
        if total != order.get_cart_total:
            return JsonResponse(
                "Un probleme est survenu lors de la verification du montant total.",
                status=404,
                safe=False,
            )
        else:
            order.transaction_id = transaction_id
            order.ip = request.META.get("REMOTE_ADDR")

        try:
            envoie_reussie = False
            keneyaton_admin_email = "admin@keneyaton.com"
            # Envoie d'un email de confirmation de commande
            confirmation_subject = "Merci pour votre Commande !"
            customer_email = request.use.email
            confirmation_message = render_to_string(
                "store/commande_confirmation.html",
                {"order": order, "customer": request.user},
            )
            send_email = EmailMessage(
                confirmation_subject,
                confirmation_message,
                keneyaton_admin_email,
                to=[customer_email],
            )
            send_email.send()
            print("Confirmation envoye")

            # Envoie d'une notification a l'administrateur du site
            notification_subject = "Vous avez reçu une nouvelle commande !"
            notification_message = render_to_string(
                "store/notification.html", {"order": order, "customer": request.user}
            )
            send_notification = EmailMessage(
                notification_subject,
                notification_message,
                keneyaton_admin_email,
                to=[keneyaton_admin_email],
            )
            send_notification.send()
            print("Notification envoye")
            envoie_reussie = True
        except Exception as e:
            print(f"Erreur lors de l'envoie de l'email: {str(e)}")
            JsonResponse(
                "Un probleme est survenu lors de l'envoie de l'email",
                status=404,
                safe=False,
            )

        if envoie_reussie:
            order.complete = True

        order.save()

        shippingAddress = ShippingAddress.objects.create(
            last_name=last_name,
            first_name=first_name,
            customer=request.user,
            order=order,
            email=email,
            phone_number=phone_number,
            country=country,
            city=city,
            street=street,
            door=door,
            company_name=compagnie,
        )
        print("Success")
    return JsonResponse("Payement effectue", safe=False)
