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

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        """This is used to override the existing update and return the status code of 200"""
        instance = self.get_object()
        # the partial true prevent the user from having to pass all fields
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=200)