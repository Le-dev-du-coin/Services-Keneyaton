from django.shortcuts import render, redirect
from store.models import Product
from django.db.models import Q


def search(request):
    if "recherche" in request.GET:
        recherche = request.GET['recherche']
        products = Product.objects.all().order_by('-create_at').filter(Q(name__icontains=recherche) | Q(description__icontains=recherche))
    context = {
        "products": products,
        "recherche": recherche
    }
    return render(request, "store/boutique.html", context)