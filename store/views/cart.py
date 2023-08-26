from django.shortcuts import render, redirect
from store.models import Customer, Category, Product, Order, OrderItem
from django.http import JsonResponse
import json
import uuid


# Cart View
def cart(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        if 'device' in request.session:
            device = request.session['device']
            customer = Customer.objects.get_or_create(customer=device)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()   
    context = {
        "items": items, 
        "order": order
        }
    return render(request, "store/panier.html", context)


# Add product in cart
def update_item(request):
    data = json.loads(request.body)
    productID = data["productID"]
    action = data["action"]

    try:
        customer = request.user.customer
    except:
        request.session['device'] = str(uuid.uuid4())
        device = request.session['device']
        customer = Customer.objects.get_or_create(customer=device)

    product = Product.objects.get(id=productID)
    order, created, = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "ajouter":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "supprimer":
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()

    # effacer le produit si la quantite est inferieur a 0
    if orderItem.quantity <= 0:
        orderItem.delete()

    if action == 'remove':
        orderItem.delete()

    return JsonResponse("Produit Ajoute", safe=False)
