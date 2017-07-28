from rest_framework import serializers
from .models import Stocks

class StockSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE
    
    class Meta:
        model = Stocks
        fields ='__all__'
        read_only_fields = ('created_at','updated_at')
        
