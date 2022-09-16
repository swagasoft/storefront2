from http.client import responses
from multiprocessing import context
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status
# Create your views here.

@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serialize = ProductSerializer(queryset, many=True, context ={'request': request})
    return Response(serialize.data)




@api_view()
def product_detail(request, id: int):
    # try:

    #     product = Product.objects.get(pk=id)
    #     serialize = ProductSerializer(product)
    #     return Response(serialize.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    product = get_object_or_404(Product, pk=id)
    serialize = ProductSerializer(product)
    return Response(serialize.data)

@api_view()
def collection_details(request, pk:int):
    return Response('ok')
