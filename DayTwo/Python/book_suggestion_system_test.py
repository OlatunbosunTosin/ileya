import unittest

import book_suggestion_system

class TestThatBookSuggestionFunctionWorks(unittest.TestCase):
        
        
    def test_that_book_page_suggest_is_between_one_and_hundred(self):
    
       self.assertTrue(book_suggestion_system.get_page_number() >= 1 and book_suggestion_system.get_page_number() <= 100)
       

    def test_that_one_book_is_added(self):
    
       expected_book_list = book_suggestion_system.add_new_books("Roses")
       actual_book_list = ["The Hobbit", "The Mystery", "Animal Farm", "Brave woman", "Roses"]
       self.assertListEqual(expected_book_list, actual_book_list)
       
       
    def test_that_one_book_is_removed(self):
    
       expected_book_list = book_suggestion_system.remove_books("Animal Farm")
       actual_book_list = ["The Hobbit", "The Mystery", "Brave woman", "Roses"]
       self.assertListEqual(expected_book_list, actual_book_list)
       
       
    def test_that_book_name_is_updated(self):
    
       expected_book_list = book_suggestion_system.update_books("Brave kingdom", "Brave woman")
       actual_book_list = ["The Hobbit", "The Mystery", "Animal Farm", "Brave woman"]
       self.assertListEqual(expected_book_list, actual_book_list)
       
       
    def test_that_all_books_is_shown(self):
    
       expected_book_list = book_suggestion_system.show_books()
       actual_book_list = ["The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom"]
       self.assertListEqual(expected_book_list, actual_book_list)
            
    
        
