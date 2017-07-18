from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Provider(models.Model):
    """
        Model representing  providers object 
    """
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    email = models.EmailField() 
    remise = models.FloatField()
    
    # Metadata
    # class Meta: 
    #     ordering = ["-my_field_name"]

  #  Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('provider-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
            def representing name and email of providers
        """
        return  "{0} -- {1} -- remise en % : {2}".format(self.name,self.email,self.remise)
    
    def _get_taux_calcul(self):
        
        return self.remise/100
    
    taux_pourcentage = property(_get_taux_calcul)


class MarketPlace(models.Model):
    """
        Model representing marketplace and their taxs
    """
    
    NAME_MARKET =(
                    ('AMZ','Amazon'),
                    ('EBY','Ebay'),
                    ('WMT','Wallmart')
        )
    
    name = models.CharField(max_length =3, choices=NAME_MARKET)
    taux = models.FloatField()
   
    
    # class Meta: 
    #     ordering = ["-my_field_name"]

    # Methods
    # def get_absolute_url(self):
    #      """
    #      Returns the url to access a particular instance of MyModelName.
    #      """
    #      return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
            String for representing the Model marketplace
        """
        return "name :{0} -- taux :{1} %".format(self.name,self.taux)
   
    def _get_taux_calcul(self):
        return self.taux/100
    
    taux_calculable = property(_get_taux_calcul)


class Product(models.Model):
    """
        Model representing the product
    """
    name = models.CharField(max_length =255, verbose_name = "nom du produit")
    marque = models.CharField(max_length =255, verbose_name = "marque du produit")
    image = models.CharField(max_length=1000, verbose_name = "image du produit", default="your img path", editable=True)
    price_HT = models.FloatField(verbose_name ="prix public HT")
    marketplace = models.ManyToManyField('MarketPlace')
    provider = models.ForeignKey(Provider,on_delete = models.SET_NULL, null=True)
    
    
    def _get_price_TTC(self):
        """ prix public TTC """
        return self.price_HT * 0.20 + self.price_HT
        
    price_TTC = property(_get_price_TTC)
    
    class Meta :
        ordering = ["name","marque"]
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of myModelName
        """
        return reverse('product-detail',args=[str(self.id)])
    
    
    def __str__(self):
        return "name :{0} -- marque :{1}".format(self.name,self.marque)
    
    
    def display_marketPlace(self):
        """
        Creates a string for the markerPlace. This is required to display marketplace in Admin.
        Because is ManyToManyField and we can display in the admin interfacez without pass by this function
        """
        return ', '.join([ marketplace.name for marketplace in self.marketplace.all()])
    display_marketPlace.short_description = 'MarketPlace'
  
  
  
        
# class Remise(models.Model):
    
#     """
#       Model representing  Remise object in fonction the Provider price
#     """
#     fournisseur = models.ForeignKey(Provider)
#     produit = models.ForeignKey(Product)
#     remise = models.IntegerField(verbose_name = "remise en %")
    
#     class Meta:
#         unique_together = ("fournisseur","produit")
    
#     def calculeRemise(self):
#         pass
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      