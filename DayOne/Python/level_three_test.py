import unittest
import level_three

class TestForLevelThreeFunctions(unittest.TestCase):

    def test_that_two_dimensional_list_is_flattened_returned(self):
    
        original_list = [[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]]
        expected_list = level_three.flatten_two_dimensional_array(original_list)
        actual_list = [9, 0, 7, 3, 5, 1, 8, 1, 7, 9, 9, 6]
        self.assertListEqual(expected_list, actual_list)
        
        original_list = [[45, 60], [33, 10, 60], [10, 33, 60]]
        expected_list = level_three.flatten_two_dimensional_array(original_list)
        actual_list = [45, 60, 33, 10, 60, 10, 33, 60]
        self.assertListEqual(expected_list, actual_list)

    def test_that_a_sort_merged_array_is_returned(self):
    
        expected_list = level_three.merging_and_sorting([3, 5, 1], [2, 4, 6])
        actual_list = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(expected_list, actual_list)
        

    def test_that_list_is_rotated_to_the_right(self):
    
        expected_list = level_three.rotate_array_by_k_positions([1, -9, 3, 0, 8] ,2)
        actual_list = [0, 8, 1, -9, 3]
        self.assertListEqual(expected_list, actual_list)
        
        expected_list = level_three.rotate_array_by_k_positions([1, -9, 3, 0, 8] , 5)
        actual_list = [1, -9, 3, 0, 8]
        self.assertListEqual(expected_list, actual_list)
        
        expected_list = level_three.rotate_array_by_k_positions([1, -9, 3, 0, 8] , 0)
        actual_list = [-9, 3, 0, 8, 1]
        self.assertListEqual(expected_list, actual_list)
        



        
