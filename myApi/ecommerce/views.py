from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
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




# class ProductViewSet(viewsets.ModelViewSet):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['Category_id', 'Brand_id']

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         results = []
#         for product in queryset:
#             results.append({
#                 "id": product.id,
#                 "name": product.name,
#                 "category": product.Category.name,
#                 "brand": product.Brand.name,
#                 "price": product.price,
#             })
#         return Response(results)


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





