import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ceaserCipherTest{
    
    
    @Test
    public void testThatMessageIsEncrypted(){

       String expectedMessage = (ceaserCipher.ceaserCipherEncryption("Help meeee!!!",7));
       assertEquals(expectedMessage, "Olsw tllll!!!");
       
       String Message = (ceaserCipher.ceaserCipherEncryption("I will win",2));
       assertEquals(Message, "K yknn ykp");
       
   
    }
    
    
    @Test
    public void testThatMessageIsDecrypted(){

       String expectedMessage = (ceaserCipher.ceaserCipherDecryption("Olsw tllll!!!",7));
       assertEquals(expectedMessage, "Help meeee!!!");
       
       String Message = (ceaserCipher.ceaserCipherDecryption("K yknn ykp",2));
       assertEquals(Message, "I will win");
       
   
    }
        
}     
       
       
         
