def get_reoccurring_numbers(number_list):

    reoccurring_list = []
    
    for count in range(len(number_list)-1):
        counter = 0
        for index in range(count+1, len(number_list)):
        
            if number_list[count] == number_list[index]:
            
                counter += 1
                
        if counter >= 1 and number_list[count] not in reoccurring_list:
            reoccurring_list.append(number_list[count])
            
    return reoccurring_list
        


def move_zeros_to_end_of_array(number_list):

    for index in range(len(number_list)-1):
    
        for count in range(index+1, len(number_list)):
        
            if number_list[index] < number_list[count]:
            
                temporary_holder = number_list[index]
                number_list[index] = number_list[count]
                number_list[count] = temporary_holder
                
    return number_list
        




