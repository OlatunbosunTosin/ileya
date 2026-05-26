import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.ArrayList;
import java.util.List;

public class BookSuggestionSystemTest{
    
    BookSuggestionSystem suggestion = new BookSuggestionSystem();
    
    @Test
    public void testThatBookPageSuggestionIsBetweenOnAndHundred(){

        assertTrue(suggestion.getPageNumber() >= 1 && suggestion.getPageNumber() <= 100);
   
    }
    
    
    @Test
    public void testThatOneBookIsAdded(){

       ArrayList<String> expectedBookList = suggestion.addNewBooks("Roses");
       ArrayList<String> actualBookList = new ArrayList<String>(List.of("The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom", "Roses"));
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    
    @Test
    public void testThatOneBookIsRemoved(){

       ArrayList<String> expectedBookList = suggestion.removeBooks("Animal Farm");
       ArrayList<String> actualBookList = new ArrayList<String>(List.of("The Hobbit", "The Mystery", "Brave kingdom"));
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    
    @Test
    public void testThatBookIsUpdted(){

       ArrayList<String> expectedBookList = suggestion.updateBooks("Animal Farm", "Animals");
       ArrayList<String> actualBookList = new ArrayList<String>(List.of("The Hobbit", "The Mystery", "Animals", "Brave kingdom"));
       assertEquals(expectedBookList, actualBookList);
   
    }
    
    @Test
    public void testThatAllBooksAreShown(){

       ArrayList<String> expectedBookList = suggestion.showBooks();
       ArrayList<String> actualBookList = new ArrayList<String>(List.of("The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom"));
       assertEquals(expectedBookList, actualBookList);
   
    }
        
}     
       
       
         
