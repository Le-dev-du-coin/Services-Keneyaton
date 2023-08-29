from django.shortcuts import render
from authentication.forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            if password1 == password2:
                user = Account.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                user.phone = phone
                user.is_customer = True
                user.save()
                message = messages.success(
                    request, "Votre compte a ete creer avec success"
                )
                return redirect("login")
            else:
                form = RegisterForm()
                messages.error(
                    request, "Un probleme est survenue verifie vos informations"
                )
                context = {
                    "form": form,
                }
    context = {"form": form}
    return render(request, "authentication/register.html", context)
