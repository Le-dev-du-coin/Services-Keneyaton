from django.db import models
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Customer
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Utilisateurs"
    )
    device = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

  

# Category
class Category(models.Model):
    name = models.CharField(max_length=180, verbose_name="Nom")
    slug = models.SlugField(blank=True)
    image = models.ImageField(
        upload_to="images/categorie",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse("category", args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


# Product
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom")
    description = models.CharField(max_length=1500)
    old_price = models.PositiveIntegerField(null=True, blank=True, verbose_name="Ancien Prix")
    new_price = models.PositiveIntegerField(verbose_name="Prix actuel")
    slug = models.SlugField(blank=True)
    image = models.ImageField(
        upload_to="products/images",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'Ajout")
    category = models.ForeignKey(
        Category, related_name="category_product", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

    @property
    def montant_en_cfa(self):
        formatted = "{:,.0f}".format(self.new_price)
        formatted = formatted.replace(',', ' ')
        return f"{formatted} F CFA"

    @property
    def montant_promo_en_cfa(self):
        formatted = "{:,.0f}".format(self.old_price)
        formatted = formatted.replace(',', ' ')
        return f"{formatted} F CFA"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


# Order
class Order(models.Model):

    # Order Status
    STATUS = (
        ('Nouvelle', 'Nouvelle'),
        ('Valider', 'Valider'),
        ('Complete', 'complete'),
        ('Annuler', 'Annuler')
    )
    PAYEMENT = (
        ('Espece', 'Espece'),
        ('Mobile Money', 'Mobile Money'),
        ('Banque', 'Banque')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Client")
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Date d'achat")
    complete = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Nouvelle')
    total = models.PositiveIntegerField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=50, choices=PAYEMENT, null=True, blank=True, verbose_name="Methode de Paiement")
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="Adresse IP")

    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Panier"

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_total_en_cfa(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        formatted = "{:,.0f}".format(total)
        formatted = formatted.replace(',', ' ')
        return f"{formatted} CFA"

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


# OrderIten
class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Produits"
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Panier")
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Quantite")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")

    class Meta:
        verbose_name = "Produits dans le Panier"
        verbose_name_plural = "Produits dans le Panier"

    def __str__(self):
        return str(self.order.transaction_id)

    @property
    def get_total(self):
        total = self.product.new_price * self.quantity
        return total

    @property
    def get_total_en_cfa(self):
        total = self.product.new_price * self.quantity
        formatted = "{:,.0f}".format(total)
        formatted = formatted.replace(',', ' ')
        return f"{formatted} F CFA"

# Shipping Address
class ShippingAddress(models.Model):
    COUNTRY_CHOICES = [
        ("Mali", "Mali"),
        ("Senegal", "Senegal"),
        ("Cote d'Ivoire", "Cote d'Ivoire"),
        ("Burkina Faso", "Burkina Faso"),
    ]

    customer = models.OneToOneField(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Client"
    )
    first_name = models.CharField(max_length=150, verbose_name="Nom")
    last_name = models.CharField(max_length=150, verbose_name="Prenom")
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, verbose_name="Contact")
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, default='Mali', verbose_name="Pays")
    city = models.CharField(max_length=150, verbose_name="Ville")
    street = models.CharField(max_length=50, verbose_name="Rue")
    door = models.IntegerField(verbose_name="Porte")
    company_name = models.CharField(max_length=200, verbose_name="Nom de la compagnie")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Panier')

    class Meta:
        verbose_name = "Adresse de livraison"
        verbose_name_plural = "Adresse de livraison"

    def __str__(self):
        return self.first_name
