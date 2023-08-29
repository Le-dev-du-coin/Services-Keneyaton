from django.contrib import admin
from authentication.models import Account


@admin.register(Account)
class Customer(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number")
    readonly_fields = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "username",
        "email",
        "password",
    )

    # Ajout Interdit
    def has_add_permission(self, obj=None):
        return False

    # Supression Interdit
    def has_delete_permission(self, request, obj=None):
        return False
