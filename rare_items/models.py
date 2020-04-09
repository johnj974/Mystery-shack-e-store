from django.db import models


class RareItem(models.Model):
    name = models.CharField(max_length=50)
    previous_owner = models.CharField(max_length=50)
    description = models.TextField()
    time_period = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name