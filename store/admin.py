from django.contrib import admin
from store.models import Customer, Category, Product, Order, OrderItem, ShippingAddress


# ------------- Mettre les produits sous leur Categorie -----------------#
class ProductInline(admin.TabularInline):
    model = Product
    readonly_fields = ['slug']
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    readonly_fields = ['slug']
# ------------- Mettre les produits sous leur Categorie -----------------#



# ------------- Mettre les produits, et l'adresse de livraison sous le panier -----------------#
class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ShippingAddressInline(admin.TabularInline):
    model = ShippingAddress
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, ShippingAddressInline]
    list_display = ('customer', 'date_ordered', 'complete', 'status', 'total', 'transaction_id', 'payment_method', 'ip')
    readonly_fields = ['customer', 'date_ordered', 'complete', 'total', 'transaction_id', 'payment_method', 'ip']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

# ------------- Mettre les paniers sous le leur proprietaire  -----------------#
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    inlines = [OrderInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

