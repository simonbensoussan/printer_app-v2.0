from rest_framework import generics
from .serializer import StockSerializer
from landing.models import Stocks


# Test with generic
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
        
class StocksDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the update,delete,get behavior of our rest api."""
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()