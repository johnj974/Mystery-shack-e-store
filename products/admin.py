from django.contrib import admin
# import the model object from models
from .models import Product

admin.site.register(Product)
