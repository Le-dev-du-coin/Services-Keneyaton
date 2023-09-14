from django.shortcuts import render, redirect
from authentication.forms import RegisterForm
from authentication.models import Account
from store.models import Customer
from django.contrib import messages


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            phone = request.POST["phone_number"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]

            user = form.save(commit=False)
            user.phone_number = phone
            user.is_customer = True
            user.save()
            customer = Customer.objects.create(
                user = user
            )

            messages.success(
                request, "Votre compte a été créer avec success"
            )
            return redirect("login")
        else:
            form = RegisterForm()
            messages.error(
                request, "Un problème est survenue vérifié vos informations"
            )
            context = {
                "form": form,
            }
    context = {"form": form}
    return render(request, "authentication/register.html", context)
