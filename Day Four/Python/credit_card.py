def credit_card_validator(card_number):

    double_number = 0
    single_digits = []
    sum_of_integers = 0
    sum_of_single_digits = 0
    sum_of_digits = 0
    sum_of_odd_places = 0
    for index in range(len(card_number)-2, -1, -2):

        double_number = int(card_number[index]) * 2
        single_digits.append(double_number)
        
    for digit in single_digits:
    
        if len(str(digit)) == 2:
        
            for number in str(digit):

                sum_of_integers += int(number)
            
        else:
            
            sum_of_single_digits += int(digit)
            
    sum_of_digits = sum_of_integers + sum_of_single_digits
    
    
    for index in range(len(card_number)-1, -1, -2):
        
        sum_of_odd_places += int(card_number[index]) 
        
    result = sum_of_digits + sum_of_odd_places
    
    
    if result % 10 == 0:
    
        validity_status = "valid"
        
    else:
    
        validity_status = "Invalid"    

    return validity_status
        



def credit_card_length(card_number):

    return len(card_number)
    


def credit_card_type(card_number):

    card_type = ""
    
    if card_number[0] == "4":
        card_type = "Visa card"
        
    elif card_number[0] == "5":
        card_type = "Mastercard"
        
    elif card_number[0] == "3" and card_number[1] == "7":
        card_type = "American Express card"
        
    elif card_number[0] == "6":
        card_type = "Discover card"
        
    else:
        card_type = "Invalid card"
        
    
    return card_type
        

        

        
        
        




