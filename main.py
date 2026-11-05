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

# determine insurance rate using down payment percent
if down_payment_percent < 10:
    insurance_rate = 5
elif down_payment_percent >= 10 < 15:
    insurance_rate = 4
elif down_payment_percent >= 15 < 20:
    insurance_rate = 3
else:
    insurance_rate = 0

# calculate down payment, insurance cost and principle amounts
down_payment_amount = (price*down_payment_percent)/100
insurance_cost = (price-down_payment_amount)*insurance_rate/100
principal_amount = price-down_payment_amount+insurance_cost

# print out the calculated results
print(f"Down payment amount is ${down_payment_amount}")
print(f"Mortgage insurance price is ${insurance_cost}")
print(f"Total mortgage amount is ${principal_amount}")