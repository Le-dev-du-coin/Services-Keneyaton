from django.shortcuts import render, redirect
from store.models import Order, OrderItem
from django.contrib.auth.decorators import login_required


# Checkout view
@login_required(login_url="register")
def checkout(request):
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
    context = {"items": items, "order": order}
    return render(request, "store/payement.html", context)


# Process to payement
@login_required(login_url="login")
def processOrder(request):
    transaction_id  = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    return JsonResponse("Payement effectue", safe=False)