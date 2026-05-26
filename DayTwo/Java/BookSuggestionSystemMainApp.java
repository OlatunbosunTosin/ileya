import java.util.Scanner;
import java.util.ArrayList;
public class BookSuggestionSystemMainApp{

    public static void main(String[] args){
    
        Scanner inputCollector = new Scanner(System.in);
    
        BookSuggestionSystem bookSuggestion = new BookSuggestionSystem();
        
        while (true){
            System.out.print(String.format(""" 
                Welcome to the Book Suggestion System!
                1. Get Suggestions
                2. Add Book
                3. Remove Book
                4. Update book
                5. Show all books
                0. Exit \n"""
        ));
    
        System.out.print("Choose an operation: ");
        int userInput = inputCollector.nextInt();
        
        if(userInput == 0){
            break;
        }
        
        switch(userInput){
        
            case 1:
                System.out.print("Book for the Day:\nBook Title: ");
                System.out.println(bookSuggestion.getBookSuggestion());
                System.out.print("Page: ");
                System.out.println(bookSuggestion.getPageNumber());
            
                System.out.print("Would you like to get another suggestion? (yes/no): ");
                String anotherSuggestion = inputCollector.next();
            
                while (anotherSuggestion.equalsIgnoreCase("yes")){
            
                    System.out.print("Book for the Day:\nBook Title: ");
                    System.out.println(bookSuggestion.getBookSuggestion());
                    System.out.print("Page: ");
                    System.out.println(bookSuggestion.getPageNumber());
                    
                    System.out.print("Would you like to get another suggestion? (yes/no): ");
                    anotherSuggestion = inputCollector.next();
        
                }
                break;
                
            case 2: 
                
                System.out.print("Enter book title: ");
                String bookName = inputCollector.next();
                bookSuggestion.addNewBooks(bookName);
                System.out.println("Book added successfully!");
                break;
                
            case 3: 
                
                System.out.print("Enter book title: ");
                String nameOfBook = inputCollector.next();
                bookSuggestion.removeBooks(nameOfBook);
                System.out.println("Book removed successfully!");
                break;
                
            case 4:

                System.out.println("Enter the old book title: ");
                String oldBookTitle = inputCollector.next();
                System.out.println("Enter the new book title: ");
                String newBookTitle = inputCollector.next();
                bookSuggestion.updateBooks(oldBookTitle, newBookTitle);
                System.out.println("Book updated successfully!");
                
            case 5:
                System.out.println("All Books");
                
                ArrayList<String> books = bookSuggestion.showBooks();
                int count = 1;
                for(String book : books){
                
                    System.out.printf("%d. %s%n", count,book);
                    count++;
                }

        }
    
    
    
        }
    
    
    }
















}
