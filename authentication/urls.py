from django.urls import path
from authentication.views import signin, register, signout

urlpatterns = [
    path("connexion/", signin.signin, name="login"),
    path("inscription/", register.register, name="register"),
    path("deconnexion/", signout.signout, name="logout"),
]
