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
    nbre_product = models.IntegerField(default= 0)
    
    # Metadata
    # class Meta: 
    #     ordering = ["-my_field_name"]

  #  Methods
    def get_absolute_url(self):
         """ Returns the url to access a particular instance of MyModelName."""
         
         return reverse('provider-detail-view', args=[str(self.id)])
    
    
    def __str__(self):
        """def representing name  of providers"""
        
        return  "{}".format(self.name.upper())
    
    
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
        return "{}".format(self.name.upper())
   
    def _get_taux_calcul(self):
        return self.taux/100
    
    taux_calculable = property(_get_taux_calcul)


class Product(models.Model):
    """
        Model representing the product
    """
    name = models.CharField(max_length =255, verbose_name = "nom du produit")
    marque = models.CharField(max_length =255, verbose_name = "marque du produit")
    image = models.CharField(max_length=10000, verbose_name = "image du produit", default="your img path", editable=True)
    price_HT = models.FloatField(verbose_name ="prix public HT")
    marketplace = models.ManyToManyField('MarketPlace')
    provider = models.ForeignKey(Provider,on_delete = models.SET_NULL, null=True)
    remise = models.FloatField()
   
    def _get_remise(self):
       "Returns la remise en %"
       return self.remise/100
    remise_in_pourcentage = property(_get_remise)
    
    def _get_prix_HT(self):
       "Returns le prix HT avec la remise comprise"
       return  self.price_HT * (1-self.remise_in_pourcentage) 
    prix_HT = property(_get_prix_HT)
    
    def _get_prix_final_TTC(self):
        "Returns the prix total de vente avec la TVA inclue"
        # TVA de 20% donc prix(1+0.20) = prix*1.20
        return  self.prix_HT * 1.20 
    prix_final_TTC = property(_get_prix_final_TTC)


     
    class Meta :
        ordering = ["name","marque"]
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of myModelName
        """
        return reverse('product-detail',args=[str(self.id)])
    
    
    def __str__(self):
        return "name :{0} -- marque :{1}".format(self.name,self.marque.upper())
    
  
    
    def display_marketPlace(self):
        """
        Creates a string for the markerPlace. This is required to display marketplace in Admin.
        Because is ManyToManyField and we can display in the admin interfacez without pass by this function
        """
        return ', '.join([ marketplace.name for marketplace in self.marketplace.all()])
    display_marketPlace.short_description = 'MarketPlace'
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      