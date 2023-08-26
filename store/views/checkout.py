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
    data = json(request.body)
    print(data)
    transaction_id  = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        first_name = data['shippingformData']['fist_name']
        last_name = data['shippingformData']['last_name']

        total = data['shippingformData']['total']
        if total != order.get_cart_total:
            return JsonResponse("Un probleme est survenu lors de la verification du montant total.")
        else:
            order.transaction_id = transaction_id
            order.ip = request.session['REMOTE_ADDR']
    return JsonResponse("Payement effectue", safe=False)