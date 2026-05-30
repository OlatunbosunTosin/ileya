from credit_card import *

card_number = input("Hello. Kindly Enter Card number to verify: ")

card_valdity_status = credit_card_validator(card_number)
card_length = credit_card_length(card_number)
card_type = credit_card_type(card_number)

print(f""" 
    Credit Card Type: {card_type}
    Credit Card Number: {card_number}
    Credit Card Digit Length: {card_length}
    Credit Card Validity Status: {card_valdity_status}
    
    """)
