import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class creditCardValidatorTest{

    creditCardValidatorFunction cardValidation = new creditCardValidatorFunction();
    
    @Test
    public void TestThatCreditCardIsValid(){
    
        String cardNumber = "5399831619690403";
        String expected = cardValidation.creditCardValidator(cardNumber);
        String actual = "valid";         
        assertEquals(expected, actual);
 
    }
    
    @Test
    public void TestThatCreditCardIsInvalid(){
    
        String cardNumber = "5399831619690404";
        String expected = cardValidation.creditCardValidator(cardNumber);
        String actual = "Invalid";         
        assertEquals(expected, actual);
 
    }


    @Test
    public void TestForCardNumberLength(){
    
        String cardNumber = "5399831619690403";
        int expected = cardValidation.creditCardLength(cardNumber);
        int actual = 16;         
        assertEquals(expected, actual);
 
    }
    
    @Test
    public void TestForCardType(){
    
        String cardNumber = "5399831619690403";
        String expected = cardValidation.creditCardType(cardNumber);
        String actual = "Mastercard";         
        assertEquals(expected, actual);
        
        
        String newCardNumber = "234319283049582";
        String expectedStatus = cardValidation.creditCardType(newCardNumber);
        String actualStatus = "Invalid card";         
        assertEquals(expectedStatus, actualStatus);
 
    }


}
