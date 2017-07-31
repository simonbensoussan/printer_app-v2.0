from django.contrib import admin
from .models import Stocks
# Register your models here.
# username = ubuntu
#password = admin123

class StockAdmin(admin.ModelAdmin):
    """Model admin for interface admin"""
    list_display = ('name','open','volume','created_at','updated_at')
    
admin.site.register(Stocks,StockAdmin)
