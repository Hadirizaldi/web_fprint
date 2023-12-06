from django.db import models

# Create your models here.

# table category
class Category(models.Model):
  category_name = models.CharField(max_length=100)

  def __str__(self):
    return self.category_name
  
# table status
class Status(models.Model):
  status_name = models.CharField(max_length=50)

  def __str__(self):
    return self.status_name

# table product
class Product(models.Model):
  product_name = models.CharField(max_length=50) 
  price = models.DecimalField(decimal_places=2, max_digits=10)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_in_category")
  status_id = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="products_with_status")

  def __str__(self):
    return self.product_name