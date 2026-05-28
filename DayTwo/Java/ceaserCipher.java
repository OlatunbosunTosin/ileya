public class ceaserCipher{

    public static String ceaserCipherEncryption(String message, int shiftKey){
    
        String encryptedMessage = "";
        String capitalAlphabets = "";
        String lowerAlphabets = "";
        
        for (int number = 65; number <= 90; number++){

            capitalAlphabets += (char) number;  
            
        }   
        
        for (int integer = 97; integer <= 122; integer++){

            lowerAlphabets += (char) integer;  
            
        }
    
        for (int index = 0; index < message.length(); index++){
        
            for (int indexes = 0; indexes < capitalAlphabets.length(); indexes++){
        
                if (Character.isLetter(message.charAt(index))){
                
                    if (message.charAt(index) == capitalAlphabets.charAt(indexes)){
                    
                        encryptedMessage += capitalAlphabets.charAt(((indexes + shiftKey) % 26));
                    
                    }
                }
                
             }  
             
             for (int indexes = 0; indexes < lowerAlphabets.length(); indexes++){
        
                if (Character.isLetter(message.charAt(index))){
                
                    if (message.charAt(index) == lowerAlphabets.charAt(indexes)){
                    
                        encryptedMessage += lowerAlphabets.charAt(((indexes + shiftKey) % 26));
                    
                    }
                
                }   
        
             }
            
            if (!Character.isLetter(message.charAt(index)))
                encryptedMessage += message.charAt(index);
            
        
        }return encryptedMessage;

    
    }
    


    public static String ceaserCipherDecryption(String encryptedMessage, int shiftKey){
    
        String decryptedMessage = "";
        String capitalAlphabets = "";
        String lowerAlphabets = "";
        
        for (int number = 65; number <= 90; number++){

            capitalAlphabets += (char) number;  
            
        }   
        
        for (int integer = 97; integer <= 122; integer++){

            lowerAlphabets += (char) integer;  
            
        }
    
        for (int index = 0; index < encryptedMessage.length(); index++){
        
            for (int indexes = 0; indexes < capitalAlphabets.length(); indexes++){
        
                if (Character.isLetter(encryptedMessage.charAt(index))){
                
                    if (encryptedMessage.charAt(index) == capitalAlphabets.charAt(indexes)){
                    
                        decryptedMessage += capitalAlphabets.charAt(((indexes - shiftKey) % 26));
                    
                    }
                
                }    
        
            }
            
            for (int indexes = 0; indexes < lowerAlphabets.length(); indexes++){
        
                if (Character.isLetter(encryptedMessage.charAt(index))){
                
                    if (encryptedMessage.charAt(index) == lowerAlphabets.charAt(indexes)){
                    
                        decryptedMessage += lowerAlphabets.charAt(((indexes - shiftKey) % 26));
                    
                    }
                
                }    
        
            }
            
            if (!Character.isLetter(encryptedMessage.charAt(index)))
                decryptedMessage += encryptedMessage.charAt(index);
            
        
        }return decryptedMessage;

    
    }



}











