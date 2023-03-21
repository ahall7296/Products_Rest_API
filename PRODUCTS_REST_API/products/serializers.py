from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields= [
            "id",
            "title",
            "description",
            "price",
            "inventory_quantity",
        ]
# fields that are not need when making post request
        read_only_fields = ["id"]