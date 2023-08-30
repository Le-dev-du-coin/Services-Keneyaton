from store.models import Customer, Order


def cart_items(request):
    cart_items = 0
    try:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        cart_items = order.get_cart_items
    except:
        if 'device' in request.session:
            device = request.session['device']
            customer, created = Customer.objects.get_or_create(device=device)
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False
            )
            cart_items = order.get_cart_items
        else:
            cart_items = 0
        
    return dict(cart_items=cart_items)
