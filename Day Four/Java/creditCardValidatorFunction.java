public class creditCardValidatorFunction{

    public String creditCardValidator(String cardNumber){

    int doubleNumber = 0;
    int [] singleDigits = new int[cardNumber.length()+1 / 2];
    int sumOfIntegers = 0;
    int sumOfSingleDigits = 0;
    int sumOfDigits = 0;
    int sumOfOddPlaces = 0;
    String validityStatus = "";
    
    int count = 0;
    for (int index = cardNumber.length() - 2; index > -1; index -= 2){

        doubleNumber = Character.getNumericValue((cardNumber.charAt(index))) * 2;
        singleDigits[count++] += doubleNumber;
        
    }
    
    for(int digit = 0; digit < singleDigits.length; digit++){  
        String digits = singleDigits[digit] + "";
        if (digits.length() == 2){

            for(int number = 0; number < digits.length(); number++){  
                sumOfIntegers += Character.getNumericValue((digits.charAt(number)));
            }
            
        }    
        else 
            sumOfSingleDigits += Integer.parseInt(digits);
            
    }
            
    sumOfDigits = sumOfIntegers + sumOfSingleDigits;
    
    

    for (int index = cardNumber.length() - 1; index > -1; index -= 2){
    
        sumOfOddPlaces += Character.getNumericValue((cardNumber.charAt(index))) ;
    }
       
    int result = sumOfDigits + sumOfOddPlaces;
    
    
    if (result % 10 == 0)
    
        validityStatus = "valid";
        
    else
    
        validityStatus = "Invalid";    

    return validityStatus;
        
    }   
    
        
    public int creditCardLength(String cardNumber){

        return cardNumber.length();

    }    

    public String creditCardType(String cardNumber){

        String cardType = "";
        
        
        if (cardNumber.charAt(0) == '4')
            cardType = "Visa card";
            
        else if (cardNumber.charAt(0) == '5')
            cardType = "Mastercard";
            
        else if (cardNumber.charAt(0) == '3' && cardNumber.charAt(1) == '7')
            cardType = "American Express card";
            
        else if (cardNumber.charAt(0) == '6')
            cardType = "Discover card";
            
        else
            cardType = "Invalid card";
            
        
        return cardType;
    }        

        
}           




