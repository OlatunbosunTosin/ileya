import unittest

import credit_card

class TestForValidityOfCreditCard(unittest.TestCase):

    def test_that_card_number_is_valid(self):
    
        card_number = "5399831619690403"
        expected = credit_card.credit_card_validator(card_number)
        actual = "valid"
        self.assertTrue(expected == actual)
        
    def test_that_card_number_is_invalid(self):
    
        card_number = "5399831619690404"
        expected = credit_card.credit_card_validator(card_number)
        actual = "Invalid"
        self.assertTrue(expected == actual)
        
    def test_for_card_number_length(self):
    
        card_number = "5399831619690403"
        expected = credit_card.credit_card_length(card_number)
        actual = 16
        self.assertTrue(expected == actual)
        
    def test_for_card_type(self):
    
        card_number = "5399831619690403"
        expected = credit_card.credit_card_type(card_number)
        actual = "Mastercard"
        self.assertTrue(expected == actual)
        
        card_number = "234319283049582"
        expected = credit_card.credit_card_type(card_number)
        actual = "Invalid card"
        self.assertTrue(expected == actual)
