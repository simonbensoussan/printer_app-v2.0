from rest_framework import serializers
from .models import Stocks

class StockSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        model = Stocks
        fields ='__all__'
        
