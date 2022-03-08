from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    product_name = models.TextField(max_length=50)
    product_category = models.TextField(max_length=50, null=True)
    product_price = models.TextField(max_length=50)