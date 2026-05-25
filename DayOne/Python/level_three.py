def flatten_two_dimensional_array(array):

    flattened_array = []
    for lists in array:
    
        for number in lists:
        
            flattened_array.append(number)
            
    return flattened_array
    
    
def rotate_array_by_k_positions(array, position):

    rotated_array = []

    rotated_array += (array[position+1 : ])
    rotated_array += (array[ : position+1])
            
    return rotated_array
        
            
    
def merging_and_sorting(array_one, array_two):

    merged_array = array_one + array_two
        
    for index in range(len(merged_array)-1):

        for count in range(index+1, len(merged_array)):
    
            if merged_array[index] > merged_array[count]:
        
                temporary_holder = merged_array[index]
                merged_array[index] = merged_array[count]
                merged_array[count] = temporary_holder
                
    return merged_array
