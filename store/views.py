from http.client import responses
from itertools import product
from multiprocessing import context
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':

        queryset = Product.objects.select_related('collection').all()
        serialize = ProductSerializer(queryset, many=True, context ={'request': request})
        return Response(serialize.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

       

        





@api_view(['GET','PUT','DELETE'])
def product_detail(request, id: int):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serialize = ProductSerializer(product)
        return Response(serialize.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def collection_details(request, pk:int):
    return Response('ok')
