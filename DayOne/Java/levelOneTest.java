import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class levelOneTest{

    @Test
    public void testThatArrayIsPalindromic(){
    
        int [] originalArray = {55, 45, 0, 8, 8, 0, 45, 55};
        assertTrue(levelOne.isPalindrome(originalArray));
   
    }

    @Test
    public void testThatArrayIsNotPalindromic(){
    
        int [] originalArray = {45, 60, 3, 10, 9, 22};
        assertFalse(levelOne.isPalindrome(originalArray));
   
    }
    
    @Test
    public void testThatPerfectSquareIsReturned(){
    
        int [] originalArray = {4, 7, 9, 10, 16, 18};
        int [] expectedArray = levelOne.getPerfectSquare(originalArray);
        int []actualArray = {4, 9, 16};
        assertArrayEquals(expectedArray, actualArray);
   
    }
    
    
    @Test
    public void testThatEvenAndOddArrayIsReturned(){
    
        int [] originalArray = {4, 7, 9, 10, 16, 18};
        int [][] expectedArray = levelOne.getEvenAndOddArray(originalArray);
        int [][]actualArray = {{7, 9}, {4, 10, 16, 18}};
        assertArrayEquals(expectedArray, actualArray);
        
            
        int [] initialArray = {45, 60, 3, 10, 9, 22};
        int [][] resultArray = levelOne.getEvenAndOddArray(initialArray);
        int [][]correctArray = {{45, 3, 9}, {60, 10, 22}};
        assertArrayEquals(resultArray, correctArray);
   
    }
    
    
    @Test
    public void testThatNonPerfectSquaresAreReplacedWithNegativeOne(){
    
        int [] originalArray = {4, 7, 9, 10, 16, 18};
        int [] expectedArray = levelOne.getNonPerfectSquare(originalArray);
        int [] actualArray = {4, -1, 9, -1, 16, -1};
        assertArrayEquals(expectedArray, actualArray);
        
            
        int [] initialArray = {45, 60, 3, 10, 9, 22};
        int [] resultArray = levelOne.getNonPerfectSquare(initialArray);
        int [] correctArray = {-1,-1,-1,-1,9,-1};
        assertArrayEquals(resultArray, correctArray);
   
    }
    
    
}     
       
