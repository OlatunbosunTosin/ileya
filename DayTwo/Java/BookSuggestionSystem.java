import java.util.Random;
import java.util.ArrayList;
import java.util.List;
public class BookSuggestionSystem{

    ArrayList<String> listOfBooks = new ArrayList<String>(List.of("The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom"));
    
    Random generator = new Random();

    public String getBookSuggestion(){

        int index = generator.nextInt(listOfBooks.size());
        return listOfBooks.get(index);
        
    }

    public int getPageNumber(){

        return generator.nextInt(1,101);

    }
        
    public ArrayList<String> addNewBooks(String bookName){

        listOfBooks.add(bookName);
        return listOfBooks;

    }

    public ArrayList<String> removeBooks(String bookName){
        
        if (listOfBooks.contains(bookName)){
        
            listOfBooks.remove(bookName);
            
        } return listOfBooks;   
    }


    public ArrayList<String> updateBooks(String oldBookName, String newBookName){

        for(int index = 0; index < listOfBooks.size(); index++){
            
            if (listOfBooks.get(index).equals(oldBookName)){
            
                listOfBooks.remove(index);
                listOfBooks.add(index, newBookName);
            
            }
            
        }return listOfBooks;

    }

    public ArrayList<String> showBooks(){

        return listOfBooks;
    
    }

    
}


