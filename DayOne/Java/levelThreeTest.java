import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class levelThreeTest{
    
    @Test
    public void testThatTwoDimensionalArrayIsFlattened(){
    
        int [][] originalArray = {{9, 0, 7}, {3, 5, 1}, {8, 1, 7}, {9, 9, 6}} ;
        int [] expectedArray = levelThree.flattenTwoDimensionalArray(originalArray);
        int []actualArray = {9, 0, 7, 3, 5, 1, 8, 1, 7, 9, 9, 6};
        assertArrayEquals(expectedArray, actualArray);
   
    }
    
    
    @Test
    public void testThatArrayIsMergedAndSorted(){
    
        int [] firstArray = {3, 5, 1};
        int [] secondArray = {2, 4, 6};
        int [] expectedArray = levelThree.mergingAndSortingArray(firstArray, secondArray);
        int [] actualArray = {1,2,3,4,5,6};
        assertArrayEquals(expectedArray, actualArray);
        
    }
    
    
 
    
}     
       
