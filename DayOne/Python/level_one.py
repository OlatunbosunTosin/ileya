import math
def is_even_and_odd(number_list):

    odd_list = []
    even_list = []
    separated_list = []
    for number in number_list:
    
        if number % 2 != 0:
            odd_list.append(number)
        else:       
            even_list.append(number)
            
    separated_list.append(odd_list)
    separated_list.append(even_list)
    
    return separated_list
    

def is_palindrome(number_list):

    initial_list = []
    initial_list += number_list
    index = 0
    for count in range(len(number_list)-1,len(number_list) // 2 ,-1):

        number_list[index] = number_list[count]

        index += 1
        
    if initial_list == number_list:
        return True
    return False
    

def is_perfect_square(number_list):

    perfect_square_numbers = []
    for number in number_list:
    
        for count in range(1,number+1):
        
            if number % count == 0 and count * count == number:

                perfect_square_numbers.append(number)
            
    return perfect_square_numbers
    
    
def negative_non_perfect_square(number_list):

    negative_non_perfect_square_numbers = []
    
    for number in number_list:
    
        for count in range(1,number+1):
        
            if number % count == 0 and count * count == number:

                negative_non_perfect_square_numbers.append(number)
                
        if number not in negative_non_perfect_square_numbers:
            negative_non_perfect_square_numbers.append(-1)     
           
    return negative_non_perfect_square_numbers

            
        

    



