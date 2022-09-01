from rest_framework import serializers
from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'optima_id', 'name', 'short_name', 'description', 'register', 'status', ]
