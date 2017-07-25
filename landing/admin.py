from django.contrib import admin
from .models import Stocks
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    """Model admin for interface admin"""
    list_display = ('name','open','volume','created_at','updated_at')
    
admin.site.register(Stocks,StockAdmin)
