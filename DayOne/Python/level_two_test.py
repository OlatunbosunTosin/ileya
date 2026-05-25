import unittest
import level_two

class TestForLevelTwoFunctions(unittest.TestCase):

    def test_that_reoccuring_numbers_in_list_is_returned(self):
    
        original_list = [45, 9, 3, 10, 9, 22]
        expected_list = level_two.get_reoccurring_numbers(original_list)
        actual_list = [9]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [45, 60, 33, 10, 60, 10, 33, 60]
        expected_list = level_two.get_reoccurring_numbers(original_list)
        actual_list = [60,33,10]
        self.assertListEqual(expected_list, actual_list)
        
    def test_that_zeros_are_moved_to_end_of_list(self):
    
        original_list = [5, 0 , 3, 0, 2, 0]
        expected_list = level_two.move_zeros_to_end_of_array(original_list)
        actual_list = [5, 3 , 2 , 0, 0 , 0]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [0, 0 , 3, 5, 2, 0, 7]
        expected_list = level_two.move_zeros_to_end_of_array(original_list)
        actual_list = [7, 5, 3 , 2 , 0, 0 , 0]
        self.assertListEqual(expected_list, actual_list)


        
