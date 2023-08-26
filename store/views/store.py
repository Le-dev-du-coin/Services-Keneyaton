from django.shortcuts import render, redirect, get_object_or_404
from store.models import Category, Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Store View
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        products_page = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.all()
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        products_page = paginator.get_page(page)
        products_count = products.count()

    context = {
        "categories": categories,
        "products": products_page,
        "products_count": products_count,
    }
    return render(request, "store/boutique.html", context)


#


# Product Detail View
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {"product": product}
    return render(request, "store/detail-produit.html", context)
