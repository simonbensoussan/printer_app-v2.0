from rest_framework import generics
from .serializer import StockSerializer
from landing.models import Stocks
from rest_framework import permissions
from landing.permissions import IsOwner

# Test with generic
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner) # ADD THIS LINE
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user) #ADD owner=self.request.user
        
class StocksDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the update,delete,get behavior of our rest api."""
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()