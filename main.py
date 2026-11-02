"""
Assignment 2 Group 7
"""

name = input("Enter client name: ")
address=input("Enter address of property: ")
price= int(input("Enter purchase price: "))


# Minimum Down Payment Component
if price <=400000:
    minimum_down_payment_percent=5
elif price <=900000:
    # percentages are written as decimals when used in this section
    percent_400k = 400000*0.05
    remainder_percent = (price-400000)*0.1
    downpayment = percent_400k+remainder_percent
    minimum_down_payment_percent = (downpayment/price)*100
else:
    minimum_down_payment_percent = 20

down_payment_percent = int(input(f"Enter down payment percentage (minimum {minimum_down_payment_percent}):"))