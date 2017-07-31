from django.test import TestCase
from landing.models import Stocks
from django.contrib.auth.models import User
#  ref : https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

class StocksTestCase(TestCase):
    """This class defines the test suite for the Stocks model."""
    @classmethod
    def setUpClassData(cls):
        # ou self
        Stocks.objects.create( name = 'SONY',open=125.05,volume=5000)
        Stocks.objects.create( name = 'KODAK',open=256.05,volume= 7000)
        Stocks.objects.create( name = 'SAMSUMG',open=125689.05,volume=845000)
        
    
    # use superuser for create an object into datbase
    # def test_model_can_create_stock(self):
    #     """Test the Stocks model can create a Stocks."""
    #     old_count = Stocks.objects.count()
    #     Stocks.objects.create( name = 'FUJITSU',open=542.25,volume=2500)
    #     new_count = Stocks.objects.count()
    #     self.assertNotEqual(old_count,new_count)
    
    def test_model_get_string_representation_object(self):
        stock = Stocks(name ='SONY')
        self.assertEqual(str(stock), stock.name)
        
"""--------------------------PERMISSION AUTHENTIFICATION REST API ------------------------------------------------"""
class ModelTestCase(TestCase):
    """This class defines the test suite for the stocklists model. REST API with Authentification"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = User.objects.create(username="ubuntu") # ADD THIS LINE
        self.stock = Stocks.objects.create( name = 'SONY',owner= self.user,open=125.05,volume=5000)
        # specify owner of a stocklist
      