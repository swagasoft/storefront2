from dataclasses import field, fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug', 'inventory','unit_price','price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(queryset=Collection.objects.all(),
    view_name='collection-detail')

    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)


