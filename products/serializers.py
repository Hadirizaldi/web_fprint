from rest_framework import serializers
from .models import Category, Product, Status

class CategorySerializer(serializers.ModelSerializer):
  class Meta :
    model = Category
    fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
  class Meta :
    model = Status
    fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
  class Meta :
    category = CategorySerializer()
    status = StatusSerializer()

    model = Product
    fields = "__all__"