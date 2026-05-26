import random

list_of_books = ["The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom"]


def get_book_Suggestion():

    return random.choice(list_of_books)
        


def get_page_number():

     return random.randint(1,100)


        
def add_new_books(book_name):

    list_of_books.append(book_name)
    return list_of_books


def remove_books(book_name):

    list_of_books.remove(book_name)
    return list_of_books



def update_books(old_book_name, new_book_name):

    list_of_books.insert(list_of_books.index(old_book_name), new_book_name)
    list_of_books.remove(old_book_name)
    return list_of_books


def show_books():

    return list_of_books
    

    



