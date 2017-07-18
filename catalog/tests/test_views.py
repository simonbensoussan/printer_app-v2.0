from django.test import TestCase

# Create your tests here

from catalog.models import Product,Provider,MarketPlace
from django.core.urlresolvers import reverse


class ProductListViewTest(TestCase):
    
    @classmethod
    def setUpClassData(cls):
        #create 13 products
        
        numbers_of_product =13
        for prod in range(numbers_of_product) :
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

def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/catalog/product/') 
        self.assertEqual(resp.status_code, 200) 

def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('product'))
        self.assertEqual(resp.status_code, 200)
        
def test_view_uses_correct_template(self):
    resp = self.client.get(reverse('product'))
    self.assertEqual(resp.status_code, 200)

    self.assertTemplateUsed(resp, 'catalog/productLis.html')