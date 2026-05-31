import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.ArrayList;


public class BookSuggestionSystemTest{
    
    BookSuggestionSystem suggestion = new BookSuggestionSystem();
    
    ArrayList<String> bookCollection = suggestion.getListOfBooks();
    
    @Test
    public void testThatBookPageSuggestionIsBetweenOnAndHundred(){

        assertTrue(suggestion.getPageNumber() >= 1 && suggestion.getPageNumber() <= 100);
   
    }
    
    
    @Test
    public void testThatOneBookIsAdded(){

       ArrayList<String> expectedBookList = suggestion.addNewBooks("Roses");
       bookCollection.add("Roses");
       ArrayList<String> actualBookList = bookCollection;
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    
    @Test
    public void testThatOneBookIsRemoved(){

       ArrayList<String> expectedBookList = suggestion.removeBooks("Animal Farm");
       bookCollection.remove("Animal Farm");
       ArrayList<String> actualBookList = bookCollection;
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    
    @Test
    public void testThatBookIsUpdated(){

       ArrayList<String> expectedBookList = suggestion.updateBooks("Animal Farm", "Animals");
       bookCollection.set(bookCollection.indexOf("Animal Farm"),"Animals");
       ArrayList<String> actualBookList = bookCollection;
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    @Test
    public void testThatAllBooksAreShown(){

       ArrayList<String> expectedBookList = suggestion.showBooks();
       
       ArrayList<String> actualBookList = bookCollection;
       assertEquals(expectedBookList, actualBookList);
   
    }
        
}     
       
       
         
