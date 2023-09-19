from django.shortcuts import render, redirect
from store.models import Order, OrderItem, ShippingAddress
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse
import json

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
    data = json.loads(request.body)
    print(data)
    transaction_id = datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        first_name = data["shippingformData"]["first_name"]
        last_name = data["shippingformData"]["last_name"]
        email = data["shippingformData"]["email"]
        phone_number = data["shippingformData"]["phone"]
        country = data["shippingformData"]["country"]
        city = data["shippingformData"]["city"]
        street = data["shippingformData"]["street"]
        door = data["shippingformData"]["door"]
        compagnie = data["shippingformData"]["compagnie"]
        payement = data["shippingformData"]["payement"]

        total = data["shippingformData"]["total"]
        total = int(total)
        if total != order.get_cart_total:
            response_data = {'error':  "Un probleme est survenu lors de la verification du montant total."}
            return JsonResponse(
               response_data,
                status=404,
                safe=False,
            )
        else:

            try:
                envoie_reussie = False
                keneyaton_admin_email = "support@services-keneyaton.com"
                # Envoie d'un email de confirmation de commande
                confirmation_subject = "Merci pour votre Commande !"
                customer_email = request.user.email
                confirmation_message = render_to_string(
                    "store/commande_confirmation.html",
                    {"order": order, "customer": request.user},
                )
                send_email = EmailMessage(
                    confirmation_subject,
                    confirmation_message,
                    keneyaton_admin_email,
                    #to=[customer_email],
                    to=['logic01pro@gmail.com']
                )
                send_email.content_subtype = "html"
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
                    #to=[keneyaton_admin_email],
                    to=['logic01pro@gmail.com']
                )
                send_notification.content_subtype = "html"
                send_notification.send()
                print("Notification envoye")
                envoie_reussie = True
            except Exception as e:
                print(f"Erreur lors de l'envoie de l'email: {str(e)}")
                response_data = {"error": "Un probleme est survenu lors de l'envoie de l'email"}
                JsonResponse(
                    response_data,
                    status=404,
                    safe=False,
                )

            shippingAddress = ShippingAddress.objects.create(
                    last_name=last_name,
                    first_name=first_name,
                    customer=request.user.customer,
                    order=order,
                    email=email,
                    phone_number=phone_number,
                    country=country,
                    city=city,
                    street=street,
                    door=door,
                    company_name=compagnie,
                )

            if envoie_reussie:
                order.transaction_id = transaction_id
                order.total = order.get_cart_total
                order.payment_method = payement
                order.ip = request.META.get("REMOTE_ADDR")
                order.complete = True
                order.save()
                shippingAddress.save()
                print("Success")
    return JsonResponse("Payement effectue", safe=False)
