import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class levelFourTest{
    
    @Test
    public void testThatIndicesOfNumbersThatSumTargetNumberIsReturned(){
    
        int [] originalArray = {2, 7, 11, 15} ;
        int [] expectedArray = levelFour.getIndicesOfSumOfTwoNumbers(originalArray, 9);
        int []actualArray = {0,1};
        assertArrayEquals(expectedArray, actualArray);
   
    }
        
}     
       
