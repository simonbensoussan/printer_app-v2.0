"""

from rest_framework.views import APIView
from rest_framework import *
from django.core.urlresolvers import reverse
from django.test import TestCase
"""
import json
from rest_framework import status
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from rest_framework.test import force_authenticate, APIClient
from django.contrib.auth.models import User

from landing.serializer import StockSerializer
from landing.models import Stocks
from landing.tests.test_models import ModelTestCase


# initialize the APIClient app
client = Client()


# class GetAllStockTest(TestCase):
#     """ Test module for GET all stocks API get the List"""
    
#     def setUp(self):
#         Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
#         Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)

#     def test_get_all_stocks(self):
#         # get API response
#         response = client.get(reverse('get_post_stock')) 
#         # get data from db
#         stocks = Stocks.objects.all()
#         serializer = StockSerializer(stocks, many=True)
#   #     self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetSingleStockTest(TestCase):
#     """ Test module for GET single object ofstock by the primary key parameter API test method GET"""

#     def setUp(self):
#         self.sony = Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
#         self.kodak = Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)
        
#     def test_get_valid_single_stock(self):
#         response = client.get(
#             reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}))
#         stock = Stocks.objects.get(pk=self.kodak.pk)
#         serializer = StockSerializer(stock)
#     #    self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_get_invalid_single_puppy(self):
#         response = client.get(
#             reverse('get_delete_update_stock', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class CreateNewStockTest(TestCase):
#     """ Test module for inserting a new object of type stock test method POST """

#     def setUp(self):
#         self.valid_payload = {
#             'name': 'KODAK',
#             'open': 256.56,
#             'volume': 8500
#         }

#         self.invalid_payload = {
#              'name': '',
#              'open': 256.56,
#              'volume': 0.001
#         }

#     def test_create_valid_post_stock(self):
#         response = client.post(
#             reverse('get_post_stock'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_invalid_post_stock(self):
#         response = client.post(
#             reverse('get_post_stock'),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class test_update_valid_method_put_stock(TestCase):
#     """ Test module for updating an existing stock record method PUT"""

#     def setUp(self):
#         self.sony = Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
#         self.kodak = Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)
        
#         self.valid_payload = {
#         'name': 'KODAK',
#         'open': 125.02,
#         'volume': 2011
#         }
    
#         self.invalid_payload = {
#         'name': ' ',
#         'open': 225.32,
#         'volume': 2500
#         }
    
#     def test_valid_update_stock_object(self):
#         response = client.put(
#         reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}),
#         data=json.dumps(self.valid_payload),
#         content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
#     def test_invalid_update_stock_object(self):
#         response = client.put(
#         reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}),
#         data=json.dumps(self.invalid_payload),
#         content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class DeleteSingleStockTest(TestCase):
#     """ Test module for deleting an existing puppy record method DELETE"""

#     def setUp(self):
#         self.sony = Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
#         self.kodak = Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)

#     def test_valid_delete_object_stock(self):
#         response = client.delete(
#             reverse('get_delete_update_stock', kwargs={'pk': self.sony.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_delete_object_stock(self):
#         response = client.delete(
#             reverse('get_delete_update_stock', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#--------------------------------------------PERMISSION AUTHENTIFICATION REST API----------------------------------------------------------------------------------------

class TestAPIAuthentificationViews(TestCase):
    """Test suite for the api views.Test with new syntax and method we use APIClient() module"""
    
    def setUp(self):
        """Define the test client and other test variables."""
        
        self.user = User.objects.create(username="ubuntu")
        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=self.user,token=None)
        # create an object Stocks example
        self.sony = Stocks.objects.create(name= 'SONY', owner= self.user,open=1235.56,volume=4500)
        
        # Since user model instance is not serializable, use its Id/PK
        # self.valid_payload = {
        #     'name': 'KODAK',
        #     'owner': self.user.id,
        #     'open': 256.56,
        #     'volume': 8500
        # }
            
    # def test_valid_create_stock_object(self):
    #     """def valid with self.valid_payload only dictionnary. TEST ERROR """
        
    #     response = client.post(
    #                             reverse('get_post_stock'),
    #                             data=json.dumps(self.valid_payload),
    #                             content_type='application/json'
    #                           )
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    # ------------------- 2nd METHOD WITH THE DICTIONNARY self.valid_payload. TEST ERROR -----------------------------------
    #     self.response = self.client.post(
    #                   reverse('get_post_stock'),
    #                   self.valid_payload,
    #                   format="json"
    #               )
    # def test_api_can_create_a_Stocks(self):
    #     """Test the api has Stocks creation capability."""
    #     self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/stocks-test/', kwargs={'pk': 3}, format="json")
        self.assertNotEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_Stocks(self):
        """Test the api can get a given Stocks."""
        stocks = Stocks.objects.get(name= 'SONY')
        response = self.client.get(
                                    reverse('get_delete_update_stock', kwargs={'pk': stocks.id})  ,  # or  '/stocks-test/', kwargs={'pk': stocks.id}, 

                                    format="json"
                                    )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, stocks)

    def test_api_can_update_Stocks(self):
        """Test the api can update a given Stocks and compare with the object initilize into the setUp() method"""
        
        stocks = Stocks.objects.get() # or  stocks = Stocks.objects.get() work too !
        change_Stocks = { 
             'name': 'FUJI',    #change the name 
             'volume': 500    #  change the volume
        }
        res = self.client.put(
                                reverse('get_delete_update_stock', kwargs={'pk': stocks.id}),
                                change_Stocks, # self.change_Stocks, 
                                format='json'
                        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        

    def test_api_can_delete_Stocks(self):
        """Test the api can delete a Stocks."""
        stocks = Stocks.objects.get()
        response = self.client.delete(
                                    reverse('get_delete_update_stock', 
                                    kwargs={'pk': stocks.id}),
                                    format='json',
                                    follow=True
                                    )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)