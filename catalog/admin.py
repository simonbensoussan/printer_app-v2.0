from django.contrib import admin
from .models import Provider,Product,MarketPlace
# Register your models here.
# username = ubuntu
#password = ubuntu123
# cutomize your admin interface create a class modelNameAdmin(admin.ModelAdmin)

class ProductAdmin(admin.ModelAdmin):
    '''
    For display the CHOICES of marketPlace you have to insert the function display_marketPlace
    '''
    list_display = ('name','marque','image','price_HT','price_TTC','provider','display_marketPlace')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email','remise')
   # fields  = ('name','surname','remise') for detail ofthe provider display the field

class MarketPlaceAdmin(admin.ModelAdmin):
      list_display = ('name','taux','taux_calculable')
    #  fields  = ('name','taux')



admin.site.register(Product,ProductAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(MarketPlace,MarketPlaceAdmin)
