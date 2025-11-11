from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer
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



# advanced => class based views ,viewsets ,routers

# first using calss based views
# from rest_framework.views import APIView

# class ProductsList(APIView):
#     def get(self,request):
#         queryset = Product.objects.all()
#         allproduct = ProductSerializer(queryset, many=True).data
#         return Response(allproduct, status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProductDetail(APIView):

#     def get_object(self,id):
#         product = get_object_or_404(Product, pk=id)
#         return product

#     def get(self,request,id):
#         product = self.get_object(id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self,request,id):
#         product = self.get_object(id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self,request,id):
#         product = self.get_object(id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#second using generic views and mixins
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class ProductsList(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'  # matches <int:id> in URL


# third using viewsets and routers

from rest_framework import viewsets
class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category_id', 'Brand_id']

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     category = self.request.query_params.get('Category_id')
    #     brand = self.request.query_params.get('Brand_id')

    #     if category:
    #         queryset = queryset.filter(Category_id=category)
    #     if brand:
    #         queryset = queryset.filter(Brand_id=brand)
    #     return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.kwargs['product_pk'])
        serializer.save(product=product)





