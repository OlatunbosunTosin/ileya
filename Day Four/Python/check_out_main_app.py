from check_out_function import *

customer_name = input("What is customer's name: ")

all_products = []
all_quantities = []
all_amounts = []
total_amount = []
sub_total = 0
index = 0

while True:

    product_bought = get_all_products()
    all_products.append(product_bought)
    
    quantity_of_product = get_quantity_of_products()
    all_quantities.append(quantity_of_product)
    
    product_amount = get_amount_of_products()
    all_amounts.append(product_amount)

    total = get_subtotal_of_purchase(quantity_of_product, product_amount)
    total_amount.append(total)
    
    sub_total += total_amount[index]
    index+=1
    
    more_items = input("Add more items? ")

    if more_items.lower() != "yes":
        break
        
cashier_name = input("What is your name: ")

discount = float(input("How much discount will he get? "))

discounted_price = (discount / 100.0) * sub_total
vat = (17.5 / 100) * sub_total
bill_total = (sub_total - discounted_price) + vat

print(f"\nSEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 08028795634\nCashier: {cashier_name}\nCustomer name: {customer_name}\n{"-"*50}\n")
print(f"{"ITEM":>10}{"QTY":>5}{"PRICE":>10}{"TOTAL(NGN)":>15}")

for count in range(len(all_products)):

    print(f"{all_products[count]:>10}{all_quantities[count]:>5}{all_amounts[count]:>10.2f}{total_amount[count]:>15.2f}\n")
print("-"*50)

print(f"{"Sub Total:":>25}{sub_total:>15.2f}\n{"Discount:":>25}{discounted_price:>15.2f}\n{"VAT @ 17.50%:":>25}{vat:>15.2f}")

print("-"*50)           
   
print(f"{"Bill Total:":>25}{bill_total:>15.2f}\n{"-"*50}\nTHIS IS NOT A RECEIPT KINDLY PAY {bill_total}\n{'-'*50}\n")

amount_paid = float(input("How much did customer give to you? "))
balance = amount_paid - bill_total

print(f"\nSEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 08028795634\nCashier: {cashier_name}\nCustomer name: {customer_name}\n{'-'*50}\n")

print(f"{"ITEM":>10}{"QTY":>5}{"PRICE":>10}{"TOTAL(NGN)":>15}")

for count in range(len(all_products)):

    print(f"{all_products[count]:>10}{all_quantities[count]:>5}{all_amounts[count]:>10.2f}{total_amount[count]:>15.2f}\n")
print('-'*50)

print(f"{"Sub Total:":>25}{sub_total:>15.2f}\n{"Discount:":>25}{discounted_price:>15.2f}\n{"VAT @ 17.50%:":>25}{vat:>15.2f}")

print("-"*50)           
   
print(f"{"Bill Total:":>25}{bill_total:>15.2f}\n{"Amount Paid:":>25}{amount_paid:>15.2f}\n{"Balance:":>25}{balance:>15.2f}\n{'-'*50}\n{"THANK YOU FOR YOUR PATRONAGE":^50}\n{'-'*50}")

