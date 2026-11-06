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

mortgage_terms = (1, 2, 3, 5, 10)
mortgage_interest_rates = (0.059, 0.058, 0.055, 0.053, 0.06)
mortgage_amortizations = (5, 10, 15, 20, 25)

# Get mortgage term
error = True
counter = 0
while error == True:
    mortgage_term = int(input('Enter mortgage term (1, 2, 3, 5, 10) '))
    for i in range(0, len(mortgage_terms)):
        if counter == len(mortgage_terms):
            print("Invalid Input")
            counter = 0
        if mortgage_terms[counter] == mortgage_term:
            index = counter
            print(index)
            error = False
        counter += 1

# Get amortization period 
error = True 
counter = 0
while error == True:
    amortization_period = int(input('Enter mortgage amortization period (5, 10, 15, 20, 25) '))
    for i in range(0, len(mortgage_amortizations)):
        if counter == len(mortgage_amortizations):
            print("Invalid Input")
            counter = 0
        if mortgage_amortizations[counter] == amortization_period:
            error = False
        counter += 1

# Calculate and output interest rate
interest_rate = mortgage_interest_rates[index]
print(f'Interest rate for the term will be {(interest_rate * 100)}%')

# Calculate and output effective monlthy interest rate
amortization = mortgage_interest_rates[index]
effective_rate = (((1 + (amortization / 2)) ** 2) ** (1 / 12)) - 1
print(f'EMR: {effective_rate}')

# Calculate and output monthly payment
monthly_payments = 12 * amortization_period
print()
monthly_payment = principal_amount * ((effective_rate * (1 + effective_rate) ** monthly_payments)) / (((1 + effective_rate) ** monthly_payments) - 1)
print(f'M: {monthly_payment}')

# Part 2 Code

