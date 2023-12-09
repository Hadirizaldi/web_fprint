from rest_framework import serializers
from products.models import Category, Product, Status

class CategorySerializer(serializers.ModelSerializer):
  class Meta :
    model = Category
    fields = '__all__'

  # def validate_category_name(self, value):
  #   """
  #   Validate whether the category name already exists in the database.
  #   """
  #   existing_category = Category.objects.filter(category_name=value).first()

  #   if existing_category:
  #     # Categories already exist, raise ValidationError
  #     raise serializers.ValidationError("Kategori sudah ada.")
    
  #   return value

class StatusSerializer(serializers.ModelSerializer):
  class Meta :
    model = Status
    fields = '__all__'

  # def validate_status_name(self, value):
  #   """
  #   Validasi apakah status sudah ada di database.
  #   """
  #   existing_status = Status.objects.filter(status_name=value).first()

  #   if existing_status:
  #     # Status sudah ada, raise ValidationError
  #     raise serializers.ValidationError("Status sudah ada.")

  #   return value

class ProductSerializer(serializers.ModelSerializer):
  class Meta :
    category = CategorySerializer()
    status = StatusSerializer()
    model = Product
    fields = '__all__'