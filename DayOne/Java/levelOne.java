import java.util.Arrays;
public class levelOne{

    public static int[][] getEvenAndOddArray(int[] numberArray){

        int countEven = 0;
        int countOdd = 0;
        for(int index = 0; index < numberArray.length; index++){
            
            if (numberArray[index] % 2 == 0)
                countEven++;
            
            if (numberArray[index] % 2 != 0)
                countOdd++;

        }
        
        int[] evenArray = new int [countEven];
        
        int[] oddArray = new int [countOdd];
        int counter = 0;
        int counts = 0;
        for(int index = 0; index < numberArray.length; index++){
            
            if (numberArray[index] % 2 == 0)
                evenArray[counter++] = numberArray[index];
            
            if (numberArray[index] % 2 != 0)
                oddArray[counts++] = numberArray[index];

        }
        
        int [][] evenOddArray = {oddArray,evenArray};
        return evenOddArray;

    
    }
    
    
    
    public static boolean isPalindrome(int[] numberArray){
    
        int[] initialArray = new int [numberArray.length];
    
        System.arraycopy(numberArray, 0, initialArray, 0, numberArray.length);
        
        int index = 0;
        for (int count = numberArray.length-1; count >= numberArray.length / 2; count--){

            int holder = numberArray[index];
            numberArray[index] = numberArray[count];
            numberArray[count] = holder;
            index += 1;
        
        }
        
        if (Arrays.equals(initialArray,numberArray))
            return true;
        return false;
    }


    public static int[] getPerfectSquare(int[] numberArray){
            
        int counter = 0;
        for(int index = 0; index < numberArray.length; index++){
        
            for (int count = 1; count <= numberArray[index]; count++){
            
                if (numberArray[index] % count == 0 && count * count == numberArray[index])
                    counter++;
                    
            }
        }
        int counts = 0;
        int [] perfectSquareNumbers = new int[counter];
        for(int index = 0; index < numberArray.length; index++){

            for (int count = 1; count <= numberArray[index]; count++){
            
                if (numberArray[index] % count == 0 && count * count == numberArray[index])
                    perfectSquareNumbers[counts++] = numberArray[index];
                    
            }
        }     
        return perfectSquareNumbers; 
            
    }
    
    
    public static int[] getNonPerfectSquare(int[] numberArray){
            
        int counts = 0;
        int [] nonPerfectSquareNumbers = new int[numberArray.length];
        for(int index = 0; index < numberArray.length; index++){

            for (int count = 1; count <= numberArray[index]; count++){
            
                if (numberArray[index] % count == 0 && count * count == numberArray[index])
                    nonPerfectSquareNumbers[counts++] = numberArray[index];
                    
            }

            if (numberArray[index] !=  nonPerfectSquareNumbers[index++])
                nonPerfectSquareNumbers[index++] = -1;
        }     
        
            
        return nonPerfectSquareNumbers; 
            
    }
    

    

}   


