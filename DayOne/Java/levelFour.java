public class levelFour{

    public static int[] getIndicesOfSumOfTwoNumbers(int[] numberArray, int target){
    
        int [] indicesArray = new int[2];
        for (int count = 0; count < numberArray.length-1; count++){
           
            for (int index  = count+1; index <  numberArray.length; index++){
                if (numberArray[count] + numberArray[index] == target){

                    indicesArray[0] = count;
                    indicesArray[1] = index;
                    
                
                }
            }
        }return indicesArray;
    }


           

}
