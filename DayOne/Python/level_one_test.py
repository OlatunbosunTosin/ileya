import unittest
import level_one

class TestForLevelOneFunctions(unittest.TestCase):

    def test_that_even_numbers_are_separated_from_odd_numbers(self):
    
        original_list = [45, 60, 3, 10, 9, 22]
        expected_list = level_one.is_even_and_odd(original_list)
        actual_list = [[45, 3 , 9] , [60 , 10, 22 ]]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [45, 60, 3, 10, 9, 22, 55, 77]
        expected_list = level_one.is_even_and_odd(original_list)
        actual_list = [[45, 3 , 9, 55, 77] , [60 , 10, 22 ]]
        self.assertListEqual(expected_list, actual_list)
        
    def test_that_list_is_not_palindromic(self):
    
        original_list = [45, 60, 3, 10, 9, 22]
        expected_list = level_one.is_palindrome(original_list)
        self.assertFalse(expected_list)
        
    def test_that_list_is_palindromic(self):
    
        original_list = [55,45, 0, 8, 8, 0, 45, 55]
        expected_list = level_one.is_palindrome(original_list)
        self.assertTrue(expected_list)
        
    def test_that_perfect_square_number_list_is_returned(self):
    
        original_list = [4, 7, 9, 10, 16, 18] 
        expected_list = level_one.is_perfect_square(original_list)
        actual_list = [4, 9, 16]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [45, 60, 3, 10, 9, 22, 21,100]
        expected_list = level_one.is_perfect_square(original_list)
        actual_list = [9, 100]
        self.assertListEqual(expected_list, actual_list)
        
    def test_that_non_perfect_square_number_are_replaced_with_negative_one(self):
    
        original_list =  [4, 7, 9, 10, 49, 6] 
        expected_list = level_one.negative_non_perfect_square(original_list)
        actual_list = [4, -1, 9, -1, 49 , -1]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [9, 22, 21,100]
        expected_list = level_one.negative_non_perfect_square(original_list)
        actual_list = [9, -1, -1, 100]
        self.assertListEqual(expected_list, actual_list)
        
