public class levelThree{

    public static int[] flattenTwoDimensionalArray(int[][] numberArray){
    
        int counter = 0;
        for (int count = 0; count < numberArray.length; count++){
           
                counter += numberArray[count].length;
                
            
        }
        
        int[] flattenedArray = new int[counter]; 
          
        int counting = 0 ;
        for (int count = 0; count < numberArray.length; count++){
            
            for (int index  = 0; index <  numberArray[count].length; index++){
                
                flattenedArray[counting++] = numberArray[count][index];
                
            }
        }
         
        return flattenedArray;
    
    
    }
  
    
    
    public static int[] mergingAndSortingArray(int[] firstArray, int[] secondArray){
    
    int[] mergedArray = new int [firstArray.length + secondArray.length];
    
    System.arraycopy(firstArray, 0, mergedArray, 0, firstArray.length);
    System.arraycopy(secondArray, 0, mergedArray, firstArray.length, secondArray.length);
    
    for (int count = 0; count < mergedArray.length-1; count++){

        for (int index  = count+1; index <  mergedArray.length; index++){
    
            if (mergedArray[count] > mergedArray[index]){
        
                int temporaryHolder = mergedArray[count];
                mergedArray[count] = mergedArray[index];
                mergedArray[index] = temporaryHolder;
            
            }
        }
    }    
        return mergedArray;

    }

    

}   


