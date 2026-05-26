import unittest
import level_four

class TestForLevelFourFunctions(unittest.TestCase):

    def test_that_indices_of_numbers_that_sum_target_number_is_returned(self):
    
        original_list = [2, 7, 11, 15]
        expected_list = level_four.get_indices_of_target_sum_numbers(original_list, 9)
        actual_list = [0,1]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [45, 10, 5, 15, 23, 10]
        expected_list = level_four.get_indices_of_target_sum_numbers(original_list,25)
        actual_list = [1,3]
        self.assertListEqual(expected_list, actual_list)
        
        
    def test_for_count_of_vowels_and_consonants(self):
    
        word = "Hello - World"
        expected_list = level_four.get_number_of_vowels_and_consonants(word)
        actual_list = ['vowels', 3, 'consonants', 7]
        self.assertListEqual(expected_list, actual_list)
        
        word = "simile metaphor"
        expected_list = level_four.get_number_of_vowels_and_consonants(word)
        actual_list = ['vowels', 6, 'consonants', 8]
        self.assertListEqual(expected_list, actual_list)
        



        
