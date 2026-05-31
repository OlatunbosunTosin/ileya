def get_all_products():

    product = input("What did the user buy? ")
    return product

def get_quantity_of_products():
    
    quantity = int(input("How many pieces? "))
    return quantity   

def get_amount_of_products():

    amount = float(input("How much per unit? "))    
    return amount
    
def get_subtotal_of_purchase(quantity, amount):

    sub_total = 0
    
    sub_total = quantity * amount
        
    return sub_total

