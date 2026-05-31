import java.util.Random;
import java.util.ArrayList;
public class BookSuggestionSystem{

    public ArrayList<String> getListOfBooks(){
    
        ArrayList<String> listOfBooks = new ArrayList<String>();
        listOfBooks.add("The Hobbit");
        listOfBooks.add("The Mystery");
        listOfBooks.add("Animal Farm");
        listOfBooks.add("Brave kingdom");
        
        return listOfBooks;
    }
    
    ArrayList<String> bookList = getListOfBooks();
    
    Random generator = new Random();

    public String getBookSuggestion(){

        int index = generator.nextInt(bookList.size());
        return bookList.get(index);
        
    }

    public int getPageNumber(){

        return generator.nextInt(1,101);

    }
        
    public ArrayList<String> addNewBooks(String bookName){

        bookList.add(bookName);
        return bookList;

    }

    public ArrayList<String> removeBooks(String bookName){
        
        if (bookList.contains(bookName)){
        
            bookList.remove(bookName);
            
        } return bookList;   
    }


    public ArrayList<String> updateBooks(String oldBookName, String newBookName){

        for(int index = 0; index < bookList.size(); index++){
            
            if (bookList.get(index).equals(oldBookName)){
            
                bookList.remove(index);
                bookList.add(index, newBookName);
            
            }
            
        }return bookList;

    }

    public ArrayList<String> showBooks(){

        return bookList;
    
    }

    
}


