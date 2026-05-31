import java.util.Scanner;
public class creditCardValidatorMainApp{

    public static void main(String[] args){
    
        creditCardValidatorFunction cardValidation = new creditCardValidatorFunction();
    
        Scanner input = new Scanner(System.in);
        System.out.print("Hello. Kindly Enter Card number to verify: ");
        String cardNumber = input.nextLine();

        String cardValdityStatus = cardValidation.creditCardValidator(cardNumber);
        int cardLength = cardValidation.creditCardLength(cardNumber);
        String cardType = cardValidation.creditCardType(cardNumber);

        System.out.print(String.format(""" 
            Credit Card Type: %s
            Credit Card Number: %s
            Credit Card Digit Length: %d
            Credit Card Validity Status: %s
            
            """, cardType, cardNumber, cardLength, cardValdityStatus
            ));
            
    }
    
}
