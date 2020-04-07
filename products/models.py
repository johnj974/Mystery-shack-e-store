from django.db import models


# tractor object
class Product(models.Model):
    name = models.CharField(max_length=50)
    horsepower = models.CharField(max_length=50)
    description = models.TextField()
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
