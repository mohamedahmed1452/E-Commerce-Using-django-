from rest_framework import serializers
from .models import Product, Category, Brand, Order, Review, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "Category", "Brand"]

    def validate_name(self, value):
        if value == "Mohamed":
            raise serializers.ValidationError("this name already existed")
        return value


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class BrandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Brand
        fields = ["id", "name", "description"]


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "product", "product_name", "quantity", "order_date"]


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "product", "product_name", "name", "description", "date"]


class TagSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ["id", "name", "products"]
