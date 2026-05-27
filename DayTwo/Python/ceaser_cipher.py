def ceaser_cipher_encryption(message, shift_key):

    encrypted_message = ""
    alphabets = ""
    for number in range(65,91):

        alphabets += chr(number)  
        
    for integer in range(97,123):

        alphabets += chr(integer) 
        

    for letter in message:

        for character in alphabets:
        
            if letter.isalpha() and letter == character:
            
                encrypted_message += alphabets[((alphabets.index(character) + shift_key) % 52)]
             
        if not letter.isalpha():
                encrypted_message += letter
                
    return encrypted_message
    


def ceaser_cipher_decryption(encrypted_message, shift_key):

    decrypted_message = ""
    alphabets = ""
    for number in range(65,91):

        alphabets += chr(number)
        
    for integer in range(97,123):

        alphabets += chr(integer)  

    for letter in encrypted_message:

        for character in alphabets:
        
            if letter.isalpha() and letter == character:
            
                decrypted_message += alphabets[((alphabets.index(character) - shift_key) % 52)]
             
        if not letter.isalpha():
                decrypted_message += letter
                
    return decrypted_message
    
