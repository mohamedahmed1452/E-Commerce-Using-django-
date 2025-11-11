from rest_framework import serializers
from .models import Product, Category, Brand, Order,Review
class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'Category', 'Brand']
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
class BrandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description']
class OrderSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'order_date']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id', 'name', 'description','date']



