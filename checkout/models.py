from django.db import models
from products.models import Product


# object for storing customer order details
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=True)
    town_or_city = models.CharField(max_length=20, blank=False)
    county = models.CharField(max_length=20, blank=False)
    eir_code = models.CharField(max_length=10, blank=False)
    contact_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


# object for item ordered
class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)  # Watch here product
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)


