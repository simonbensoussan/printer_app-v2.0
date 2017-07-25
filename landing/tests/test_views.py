"""
from rest_framework.test import *
from rest_framework.views import APIView
from rest_framework import *
from django.core.urlresolvers import reverse
from django.test import TestCase
"""
import json
from rest_framework import status
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from ..serializer import StockSerializer
from landing.models import Stocks

# initialize the APIClient app
client = Client()


class GetAllStockTest(TestCase):
    """ Test module for GET all stocks API get the List"""
    
    def setUp(self):
        Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
        Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)

    def test_get_all_stocks(self):
        # get API response
        response = client.get(reverse('get_post_stock'))
        # get data from db
        stocks = Stocks.objects.all()
        serializer = StockSerializer(stocks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppyTest(TestCase):
    """ Test module for GET single object ofstock by the primary key parameter API test method GET"""

    def setUp(self):
        self.sony = Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
        self.kodak = Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)
        
    def test_get_valid_single_stock(self):
        response = client.get(
            reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}))
        stock = Stocks.objects.get(pk=self.kodak.pk)
        serializer = StockSerializer(stock)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_invalid_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_stock', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPuppyTest(TestCase):
    """ Test module for inserting a new object of type stock test method POST """

    def setUp(self):
        self.valid_payload = {
            'name': 'KODAK',
            'open': 256.56,
            'volume': 8500
        }

        self.invalid_payload = {
             'name': ' ',
             'open': 256.56,
             'volume': 0.001
        }

    def test_create_valid_post_stock(self):
        response = client.post(
            reverse('get_post_stock'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_post_stock(self):
        response = client.post(
            reverse('get_post_stock'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class test_update_valid_method_put_stock(TestCase):
    """ Test module for updating an existing stock record """

    def setUp(self):
        self.sony = Stocks.objects.create(name= 'SONY',open=1235.56,volume=4500)
        self.kodak = Stocks.objects.create(name= 'KODAK',open=256.56,volume=8500)
        
        self.valid_payload = {
        'name': 'KODAK',
        'open': 125.02,
        'volume': 2011
        }
    
        self.invalid_payload = {
        'name': ' ',
        'open': 225.32,
        'volume': 2500
        }
    
    def test_valid_update_stock_object(self):
        response = client.put(
        reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}),
        data=json.dumps(self.valid_payload),
        content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_update_stock_object(self):
        response = client.put(
        reverse('get_delete_update_stock', kwargs={'pk': self.kodak.pk}),
        data=json.dumps(self.invalid_payload),
        content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
