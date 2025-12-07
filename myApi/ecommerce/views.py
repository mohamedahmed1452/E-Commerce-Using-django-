from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product, Review, Category, Brand, Order
from .serializers import (
    ProductSerializer,
    ReviewSerializer,
    CategorySerializer,
    BrandSerializer,
    OrderSerializer,
)
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework import viewsets


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        allproduct = ProductSerializer(queryset, many=True)
        return Response(data=allproduct.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductClassBasedView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"message": "Product Updated Successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(
            data={"message": "Product Deleted Successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"message": "Product Partially Updated Successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class AllProductClassBasedView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        allproduct = ProductSerializer(queryset, many=True)
        return Response(data=allproduct.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListCreateProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["product", "quantity"]
    search_fields = ["product__name"]
    ordering_fields = ["order_date", "quantity"]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["product", "name"]
    search_fields = ["name", "description", "product__name"]
    ordering_fields = ["date", "name"]


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["product"]
    search_fields = ["product__name"]
    ordering_fields = ["order_date"]


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["product"]
    search_fields = ["name", "product__name"]
    ordering_fields = ["date"]


""" Conclusion
From the Silk profiling results, the http://127.0.0.1:8000/api/products/?Category_id=5 endpoint shows a clear difference in performance between two runs.

The unoptimized version executed 28 SQL queries, taking 559 ms overall, with more time spent on individual queries.

After optimization, the query count dropped to 9 queries, and the total response time decreased to 374 ms.
"""


""" Conclusion Summary
Using Django ORM with related models (Category, Brand, Product), we demonstrated the N+1 query problem.  
- The **unoptimized endpoint** executed one query per product (28 total queries).  
- The **optimized endpoint** using `select_related()` reduced it to only **1 query** via JOINs.  
- Response time dropped by nearly 40%.  
- For many-to-many relations, `prefetch_related()` further optimizes performance.

This proves ORM-level query optimization significantly improves scalability and efficiency in Django applications.
"""


# Lab Session Three

# 1. Build Dynamic Filter Query using Q() Expressions
# from django.db.models import Q
# from ecommerce.models import Product

# dynamic_products = Product.objects.filter(
#     Q(Category__name="Electronics") & Q(price__gt=500)
# )

# for p in dynamic_products:
#     print(p.name, p.price, p.Category.name)


# 2. Update Fields Directly in SQL using F() Expressions
# from django.db.models import F
# Product.objects.update(price=F('price') * 1.1)


# 3. Select Specific Fields using only() and defer()

# Fetch only name and price fields  =>only()
# qs = Product.objects.only('name', 'price')

# for p in qs:
#     print(p.name, p.price) # no extra query


# Fetch everything except the 'description' field  =>defer()
# qs = Product.objects.defer('description')

# for p in qs:
#     print(p.name)  # no extra query


# 4. Retrieve Data as Dictionary (.values()) and Tuple (.values_list())

# As dictionary
# qs_dict = Product.objects.values('id', 'name', 'price', 'Category__name')
# print(list(qs_dict)[:3])

# # As tuple
# qs_tuple = Product.objects.values_list('name', 'price')
# print(list(qs_tuple)[:3])


# 5. Apply Index on Proper Fields
# class Product(models.Model):
#     name = models.CharField(max_length=255, db_index=True)   # indexed field
#     price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
#     Category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


# 6. Compare Performance Between Indexed vs Non-Indexed Fields

# from django.db import connection
# from time import perf_counter

# Indexed field query
# start = perf_counter()
# list(Product.objects.filter(price__gte=100))
# end = perf_counter()
# print("Indexed field time:", end - start)
# print("Queries:", len(connection.queries))

# Non-indexed field query (like description)
# start = perf_counter()
# list(Product.objects.filter(description__icontains='phone'))
# end = perf_counter()
# print("Non-indexed field time:", end - start)
# print("Queries:", len(connection.queries))

# 7. Change Connection Max Age and Observe

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         'CONN_MAX_AGE': 60,  # keep DB connection open for 60 seconds
#     }
# }
