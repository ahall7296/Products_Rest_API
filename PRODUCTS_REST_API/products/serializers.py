from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= [
            "id",
            "title",
            "description",
            "price",
            "inventory_quantity",
            "picture"
        ]
# fields that are not need when making post request
        read_only_fields = ["id"]