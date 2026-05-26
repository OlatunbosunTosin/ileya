def get_indices_of_target_sum_numbers(number_list, target):
    
    for count in range(len(number_list)-1):
       
        for index in range(count+1, len(number_list)):
        
            if number_list[count] + number_list[index] == target:
            
                return [count, index]
                


def get_number_of_vowels_and_consonants(word):

    vowel_count = 0
    consonant_count = 0
    vowel = "aeiou"
    
    for letter in word.lower():
    
        if letter.isalpha():
            if letter in vowel:
        
                vowel_count += 1
    
            else:
                consonant_count += 1
                
    return ["vowels", vowel_count, "consonants", consonant_count]
    

    
        




