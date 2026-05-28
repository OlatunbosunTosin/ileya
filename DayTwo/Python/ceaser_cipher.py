def ceaser_cipher_encryption(message, shift_key):

    encrypted_message = ""
    capital_alphabets = ""
    lower_alphabets = ""
    
    for number in range(65,91):

        capital_alphabets += chr(number)  
        
    for integer in range(97,123):

        lower_alphabets += chr(integer) 
        

    for letter in message:

        for capital_character in capital_alphabets:
        
            if letter.isalpha() and letter == capital_character:
            
                encrypted_message += capital_alphabets[((capital_alphabets.index(capital_character) + shift_key) % 26)]
           
        for lower_character in lower_alphabets:
        
            if letter.isalpha() and letter == lower_character:
            
                encrypted_message += lower_alphabets[((lower_alphabets.index(lower_character) + shift_key) % 26)]  
        if not letter.isalpha():
                encrypted_message += letter
                
    return encrypted_message
    


def ceaser_cipher_decryption(encrypted_message, shift_key):

    decrypted_message = ""
    capital_alphabets = ""
    lower_alphabets = ""
    
    for number in range(65,91):

        capital_alphabets += chr(number)
        
    for integer in range(97,123):

        lower_alphabets += chr(integer)  

    for letter in encrypted_message:

        for capital_character in capital_alphabets:
        
            if letter.isalpha() and letter == capital_character:
            
                decrypted_message += capital_alphabets[((capital_alphabets.index(capital_character) - shift_key) % 26)]
                
        for lower_character in lower_alphabets:
        
            if letter.isalpha() and letter == lower_character:
            
                decrypted_message += lower_alphabets[((lower_alphabets.index(lower_character) - shift_key) % 26)] 
             
        if not letter.isalpha():
                decrypted_message += letter
                
    return decrypted_message
    
