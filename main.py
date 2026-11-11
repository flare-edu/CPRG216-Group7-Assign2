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

down_payment_percent = float(input(f"Enter down payment percentage (minimum {minimum_down_payment_percent}): "))

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
    mortgage_term = int(input('Enter mortgage term (1, 2, 3, 5, 10): '))
    for i in range(0, len(mortgage_terms)):
        if counter == len(mortgage_terms):
            print("Invalid Input")
            counter = 0
        if mortgage_terms[counter] == mortgage_term:
            index = counter
            # note print(index)
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
# note print(f'EMR: {effective_rate}')

# Calculate and output monthly payment
monthly_payments = 12 * amortization_period
print()
monthly_payment = principal_amount * ((effective_rate * (1 + effective_rate) ** monthly_payments)) / (((1 + effective_rate) ** monthly_payments) - 1)
print(f'Monthly Payment Amount is: {monthly_payment}')

# Part 2 Code

output_monthly_chart = input('Would you like to see the amortization schedule? (Y/N): ')

if output_monthly_chart.upper() == 'Y':
    # convenient list for the relevant data needed for every month
    # each entry is a dictionary
    monthly_interest_list = []

    # this will be updated every time we loop to track how much is left to pay
    # starts at total mortgage value
    last_closing_balance = principal_amount
    for i in range(0, 12 * mortgage_term):
        # It's a dictionary, because no objects yet
        month_entry ={
            # which month this entry represents
            "month_no":i+1,
            # how much is owed at the start of the month
            "opening_bal":last_closing_balance,
            # how much is owed after the month is paid for
            "closing_bal":0,
            # total interest needing to be paid this month
            "interest":0,
            # total payment without interest
            "principle":0,
            # amount needing to be paid
            "payment": monthly_payment
        }
        # get total interest
        month_entry["interest"] = month_entry["opening_bal"] * effective_rate
        # get principle amount
        month_entry["principle"] = monthly_payment - month_entry["interest"]
        # set closing bal
        last_closing_balance = month_entry["opening_bal"] - month_entry["principle"]
        month_entry["closing_bal"] = last_closing_balance
        # Append to MLI and move to next month
        monthly_interest_list.append(month_entry)

    print('Month    Opening Bal        Payment      Principal       Interest    Closing Bal')
    interest_list_iterator = 0
    for i in monthly_interest_list:
        print(f'{monthly_interest_list[interest_list_iterator].get('month_no'):>5} {monthly_interest_list[interest_list_iterator].get('opening_bal'):>14.2f} {monthly_interest_list[interest_list_iterator].get('payment'):>14.2f} {monthly_interest_list[interest_list_iterator].get('principle'):>14.2f} {monthly_interest_list[interest_list_iterator].get('interest'):>14.2f} {monthly_interest_list[interest_list_iterator].get('closing_bal'):>14.2f}')
        interest_list_iterator += 1