from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        allproduct = ProductSerializer(queryset, many=True).data
        return Response(allproduct, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        print('data = ',serializer)
        serializer.is_valid(raise_exception=True)
        product =serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

# advanced => class based views ,viewsets ,routers

#first using calss based views
from rest_framework.views import APIView

class ProductsList(APIView):
    def get(self,request):
        queryset = Product.objects.all()
        allproduct = ProductSerializer(queryset, many=True).data
        return Response(allproduct, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)# convert json to object ex => before convert json to object ==> {'name':'product1','description':'desc1','price':100,'Category':1,'Brand':1} after convert json to object ==> <Product: Product object (1)>
        print('data = ',serializer)
        serializer.is_valid(raise_exception=True)
        product =serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





