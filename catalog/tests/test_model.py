from django.test import TestCase

# Create your tests here

from catalog.models import Product,Provider,MarketPlace


class ProductModelTest(TestCase):
    
    @classmethod
    def setUpClassData(cls):
        
       #Set up non-modified objects used by all test method
        provider = Provider.objects.create(
                                        name ="pearl",
                                        surname="ppopo",
                                        email="contact@peral.net",
                                        remise= 13.56
                                            )
        market = MarketPlace.objects.create(
                                        name="AMZ",
                                        taux = 5.6
                                        )
     
        product = Product.objects.create(
                                        name="SI98778",
                                        marque="KODAK",
                                        image="https://www.google.fr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjbtLHfyJDVAhVE6xQKHeVRAMQQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FKodak-ScanMate-I1150-Sheetfed-Scanner%2Fdp%2FB00LSO6CSQ&psig=AFQjCNHWINsGMYPOrIgUfJI0FcqATQ8i5g&ust=1500389538238195",
                                        price_HT =235.32,
                                        provider = provider
                                        )
        product.marketplace.add(market)                                  
                                        
    def test_first_name_label(self):
        # test pass OK
        try :
            product = Product.objects.get(id=1)
            field_label = product._meta.get_field('name').verbose_name
            self.assertEquals(field_label,'nom du produit')
        except Product.DoesNotExist:
            product = None
    
    def test_first_name_max_length(self):
        
        try:
            product = Product.objects.get(id=1)
            max_length = product._meta.get_field('name').max_length
            self.assertEquals(max_length,255)
        except Product.DoesNotExist:
            product = None
    
    def test_image_max_length(self):
        
        try:
            product = Product.objects.get(id=1)
            max_length = product._meta.get_field('image').max_length
            self.assertEquals(max_length,1000)
        except Product.DoesNotExist:
            product = None

    def test_get_absolute_url(self):
        try:
            product = Product.objects.get(id=1)
            self.assertEquals(product.get_absolute_url(),'/catalog/product/1')
        except Product.DoesNotExist:
            product = None
            
            
        
        
        