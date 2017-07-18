# from django.test import TestCase

# # Create your test here

# class YourTestClass(TestCase):
#     '''
#     Class Test example
#     '''
    
#     @classmethod
#     def setUpTestData(cls):
       
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#          #Setup run before every test method.
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

# #   def tearDown(self):
#         #Clean up run after every test method.
#   #     pass
   
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)