""" 
 .https://realpython.com/blog/python/test-driven-development-of-a-django-restful-api/
 .Second way to codez the view
 .TODO SEARCH THE SAME THING WITH GENERIC
MEMO GET = lister, DELETE = effacer, PUT = mise a jour, POST = Creer

"""

from django.shortcuts import render
from rest_framework import generics
from .serializer import StockSerializer
from landing.models import Stocks
# Create your views here.
# import for the second way to test API an other method 'decorator' for the api_view see the documentation rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions,generics
from landing.permissions import IsOwner

# Test with generic
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner) # ADD THIS LINE
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user) # ADD owner=self.request.user
        
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
     
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)
    
    
"""------------------- METHOD TWO FOR CREATE REST API VIEWS WITHOUT GENERIC -------------------------"""

# test without generic views
# with the decorator mode. module name api_views.
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_stock(request, pk):
    try:
        stock = Stocks.objects.get(pk=pk)
    except Stocks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single stock
    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)
    # delete a single stock
    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       # for testing return Response({})
       
    # update details of a single stock
    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_stock(request):
    # get all stocks voir tuto newboston rest api
    if request.method == 'GET':    
       stocks = Stocks.objects.all()
       serializer = StockSerializer(stocks, many=True)
       return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == 'POST':
         data = {
            'name': request.data.get('name'),
            'open': request.data.get('open'),
            'volume': request.data.get('volume')
        }
         serializer = StockSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
