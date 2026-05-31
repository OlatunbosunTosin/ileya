import unittest

from check_out_function import *

quantity_bought = get_quantity_of_products()
amount_of_product = get_amount_of_products()

class TestThatCheckOutFunctionWorks(unittest.TestCase):

    
    def test_that_product_item_is_returned(self):
    
        product = input("Enter product: ")
        self.assertEqual(get_all_products(),product)
        
    def test_that_quantity_of_item_is_returned(self):
    
        quantity = int(input("Enter quantity of product: "))
        self.assertEqual(quantity_bought,quantity)
        
    def test_that_amount_of_item_is_returned(self):
    
        amount = float(input("Enter amount of product: "))
        self.assertEqual(amount_of_product,amount)
        
    def test_that_total_of_item_is_returned(self):
    
        total = quantity_bought * amount_of_product
        self.assertEqual(get_subtotal_of_purchase(quantity_bought, amount_of_product),total)


