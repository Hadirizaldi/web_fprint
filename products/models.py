from django.db import models

# Create your models here.

# table category
class Category(models.Model):
  category_name = models.CharField(max_length=100)

# table status
class Status(models.Model):
  status_name = models.CharField(max_length=50)

# table product
class Product(models.Model):
  product_name = models.CharField(max_length=50) 
  price = models.DecimalField(decimal_places=2, max_digits=10)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
  status_id = models.ForeignKey(Status, on_delete=models.CASCADE)