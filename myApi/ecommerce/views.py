from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.all()
#         allproduct = ProductSerializer(queryset, many=True).data
#         return Response(allproduct, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         print('data = ',serializer)
#         serializer.is_valid(raise_exception=True)
#         product =serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
# @api_view(['GET','PUT','DELETE'])
# def product_detail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer



import cProfile
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

def profiled_product_list(request):
    profiler = cProfile.Profile()
    profiler.enable()

    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data

    profiler.disable()
    profiler.print_stats(sort='time')

    return JsonResponse(data, safe=False)






class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category_id', 'Brand_id']

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        results = []
        for product in queryset:
            results.append({
                "id": product.id,
                "name": product.name,
                "category": product.Category.name,
                "brand": product.Brand.name,
                "price": product.price,
            })

        return Response(results)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('Category', 'Brand').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category_id', 'Brand_id']
   



''' Conclusion
From the Silk profiling results, the http://127.0.0.1:8000/api/products/?Category_id=5 endpoint shows a clear difference in performance between two runs.

The unoptimized version executed 28 SQL queries, taking 559 ms overall, with more time spent on individual queries.

After optimization, the query count dropped to 9 queries, and the total response time decreased to 374 ms.
'''










class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.kwargs['product_pk'])
        serializer.save(product=product)



#Lab Session Two

@api_view(['GET'])
def unoptimized_products(request):
    queryset = Product.objects.all()  
    results = []
    for product in queryset:
        results.append({
            "id": product.id,
            "name": product.name,
            "category": product.Category.name,
            "brand": product.Brand.name,
        })
    return Response(results)


@api_view(['GET'])
def optimized_products(request):
    queryset = Product.objects.select_related('Category', 'Brand').all()
    results = []
    for product in queryset:
        results.append({
            "id": product.id,
            "name": product.name,
            "category": product.Category.name,
            "brand": product.Brand.name,
        })
    return Response(results)

@api_view(['GET'])
def optimized_with_prefetch(request):
    queryset = Product.objects.select_related('Category', 'Brand').prefetch_related('tags').all()

    results = []
    for product in queryset:
        results.append({
            "id": product.id,
            "name": product.name,
            "category": product.Category.name,
            "brand": product.Brand.name,
            "tags": [tag.name for tag in product.tags.all()]  # ✅ already prefetched
        })
    return Response(results)


''' Conclusion Summary
Using Django ORM with related models (Category, Brand, Product), we demonstrated the N+1 query problem.  
- The **unoptimized endpoint** executed one query per product (28 total queries).  
- The **optimized endpoint** using `select_related()` reduced it to only **1 query** via JOINs.  
- Response time dropped by nearly 40%.  
- For many-to-many relations, `prefetch_related()` further optimizes performance.

This proves ORM-level query optimization significantly improves scalability and efficiency in Django applications.
'''



#Lab Session Three

#1. Build Dynamic Filter Query using Q() Expressions
from django.db.models import Q
from ecommerce.models import Product

dynamic_products = Product.objects.filter(
    Q(Category__name="Electronics") & Q(price__gt=500)
)

for p in dynamic_products:
    print(p.name, p.price, p.Category.name)


#2. Update Fields Directly in SQL using F() Expressions
from django.db.models import F
Product.objects.update(price=F('price') * 1.1)



#3. Select Specific Fields using only() and defer()

# Fetch only name and price fields  =>only()
qs = Product.objects.only('name', 'price')

for p in qs:
    print(p.name, p.price) # no extra query



# Fetch everything except the 'description' field  =>defer()
qs = Product.objects.defer('description')

for p in qs:
    print(p.name)  # no extra query


#4. Retrieve Data as Dictionary (.values()) and Tuple (.values_list())

# As dictionary
qs_dict = Product.objects.values('id', 'name', 'price', 'Category__name')
print(list(qs_dict)[:3]) 

# As tuple
qs_tuple = Product.objects.values_list('name', 'price')
print(list(qs_tuple)[:3])  


#5. Apply Index on Proper Fields
# class Product(models.Model):
#     name = models.CharField(max_length=255, db_index=True)   # indexed field
#     price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
#     Category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


#6. Compare Performance Between Indexed vs Non-Indexed Fields

from django.db import connection
from time import perf_counter

# Indexed field query
start = perf_counter()
list(Product.objects.filter(price__gte=100))
end = perf_counter()
print("Indexed field time:", end - start)
print("Queries:", len(connection.queries))

# Non-indexed field query (like description)
start = perf_counter()
list(Product.objects.filter(description__icontains='phone'))
end = perf_counter()
print("Non-indexed field time:", end - start)
print("Queries:", len(connection.queries))

#7. Change Connection Max Age and Observe

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         'CONN_MAX_AGE': 60,  # keep DB connection open for 60 seconds
#     }
# }