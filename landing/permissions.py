from rest_framework.permissions import BasePermission
from landing.models import Stocks

class IsOwner(BasePermission):
    """Custom permission class to allow only StockList owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the StockList owner."""
        if isinstance(obj, Stocks):
            return obj.owner == request.user
        return obj.owner == request.user