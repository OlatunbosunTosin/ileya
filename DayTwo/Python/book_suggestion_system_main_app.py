from book_suggestion_system import *

while True:
    print(""" 
    Welcome to the Book Suggestion System!
    1. Get Suggestions
    2. Add Book
    3. Remove Book
    4. Update book
    5. Show all books
    6. Exit

""")

    user_input = int(input("Choose an operation: "))
 
    match user_input:
        
        case 1:
            print("Book for the Day:\nBook Title: ", end ="")
            print(get_book_Suggestion())
            print("Page: ", end ="")
            print(get_page_number())
            
            another_suggestion = input("Would you like to get another suggestion? (yes/no): ")
            
            while (another_suggestion.lower() == "yes"):
            
                print("Book for the Day:\nBook Title: ", end ="")
                print(get_book_Suggestion())
                print("Page: ", end ="")
                print(get_page_number())
                
                another_suggestion = input("Would you like to get another suggestion? (yes/no): ")
                
        case 2:
            
            book_title = input("Enter the book title: ")
            add_new_books(book_title)
            print("Book added successfully!")
            
        case 3:

            book_title = input("Enter the book title to remove: ")
            remove_books(book_title)
            print("Book removed successfully!")
            
            
        case 4:

            old_book_title = input("Enter the old book title: ")
            new_book_title = input("Enter the new book title: ")
            update_books(old_book_title, new_book_title)
            print("Book updated successfully!")
            
        case 5:
            print("All Books")
            count = 1
            for elements in show_books():
                print(f"{count}. {elements}")
                count+=1
            
        case 6:
            break
                
                
        
