from django.shortcuts import render
from store.models import Category, Product
from django.core.mail import EmailMessage
from django.contrib import messages


def home(request):
    categories = Category.objects.order_by("name")[:6]
    popular_products = Product.objects.filter(is_popular=True).order_by("-create_at")[:20]
    new_arrivage = Product.objects.filter(is_new_arrivage=True).order_by('-create_at')[:20]

    context = {
        "categories": categories,
        "popular_products": popular_products,
        'new_arrivage': new_arrivage,
    }
    return render(request, "core/index.html", context)


def contact(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        subject_formatted = f"Vous avez recu un nouveau message de la part de {full_name} depuis votre site"
        try:
            send_email = EmailMessage(
                subject_formatted, message, email, to=["dembasylla779@gmail.com"]
            )
            send_email.send()
            messages.success(
                request,
                "Votre email a ete envoyer avec success. Nous serons ravi de vous lire.",
            )
        except Exception as e:
            print(f"Echec d'envoie d'email: {str(e)}")
            messages.error(request, "Echec d'envoie de message. Veuillez reessayer")

    return render(request, "core/contact.html")
