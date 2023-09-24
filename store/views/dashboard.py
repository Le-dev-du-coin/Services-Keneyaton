from django.shortcuts import render
from store.models import Order


def dashboard(request):
    my_order = Order.objects.filter(customer=request.user.customer, complete=True).order_by('-date_ordered')
    context = {
        "my_order": my_order
    }
    return render(request, "store/dashboard.html", context)