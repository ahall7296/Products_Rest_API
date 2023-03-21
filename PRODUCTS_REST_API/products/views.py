from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    """
    this list all products available base on the queryset provided
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

