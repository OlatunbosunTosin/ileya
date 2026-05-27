public class ceaserCipher{

    public static String ceaserCipherEncryption(String message, int shiftKey){
    
        String encryptedMessage = "";
        String alphabets = "";
        
        for (int number = 65; number <= 90; number++){

            alphabets += (char) number;  
            
        }   
        
        for (int integer = 97; integer <= 122; integer++){

            alphabets += (char) integer;  
            
        }
    
        for (int index = 0; index < message.length(); index++){
        
            for (int indexes = 0; indexes < alphabets.length(); indexes++){
        
                if (Character.isLetter(message.charAt(index))){
                
                    if (message.charAt(index) == alphabets.charAt(indexes)){
                    
                        encryptedMessage += alphabets.charAt(((indexes + shiftKey) % 52));
                    
                    }
                
                }    
        
            }
            if (!Character.isLetter(message.charAt(index)))
                encryptedMessage += message.charAt(index);
            
        
        }return encryptedMessage;

    
    }
    


    public static String ceaserCipherDecryption(String encryptedMessage, int shiftKey){
    
        String decryptedMessage = "";
        String alphabets = "";
        
        for (int number = 65; number <= 90; number++){

            alphabets += (char) number;  
            
        }   
        
        for (int integer = 97; integer <= 122; integer++){

            alphabets += (char) integer;  
            
        }
    
        for (int index = 0; index < encryptedMessage.length(); index++){
        
            for (int indexes = 0; indexes < alphabets.length(); indexes++){
        
                if (Character.isLetter(encryptedMessage.charAt(index))){
                
                    if (encryptedMessage.charAt(index) == alphabets.charAt(indexes)){
                    
                        decryptedMessage += alphabets.charAt(((indexes - shiftKey) % 52));
                    
                    }
                
                }    
        
            }
            if (!Character.isLetter(encryptedMessage.charAt(index)))
                decryptedMessage += encryptedMessage.charAt(index);
            
        
        }return decryptedMessage;

    
    }



}











