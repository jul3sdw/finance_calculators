#finance_calculators.py
#Written by: Julian de Wet
#Written on: 11/02/2020
#Task 12
#Program asks whether you are investing or repaying a bond and calculates the interest or bond repayments based off what the user enters

import math
#Prints instructions for the user to follow
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\ninvestment\t - to calculate the amount of interest you'll earn on interest\nbond\t\t - to calculate the amount you'll have to pay on a home loan")

#User chooses "investment" or "bond"
menu_choice = input("Your choice: ")

#If statement that decides based off the user input which calculation must be done
#The statement also outputs an apropriate error code if necessary 
if menu_choice.lower() == "":
    print("You did not enter a choice") 

#If statement gathers information on the deposit and type of interest
elif menu_choice.lower() == "investment":
    deposit = input("How much money are you depositing: ")
    interest_rate = input("What is your interest rate percentage: ")
    interest_rate_strip = interest_rate.strip("%")
    interest_rate_float = float(interest_rate_strip) / 100.00
    years = input("How many years do you plan on investing for: ")
    interest_type = input("Simple or compound interest: ")

#if statement calculates simple interest
    if interest_type.lower() == "simple":
        simple_interest = float(deposit) * (1 + interest_rate_float * int(years)) 
        print(f"You will earn R{simple_interest:.2f}")
    
#if statement calculates compound interest
    elif interest_type.lower() == "compound":
        compound_interest = float(deposit) * math.pow((1 + interest_rate_float),int(years))
        print(f"R{compound_interest:.2f}")

#else statement ouputs an error message
    else:
        print("You did not enter a valid option")

#if statement asks for information about the bond and calculates the repayments
elif menu_choice.lower() == "bond": 
    present_value = input("What is the current value of the house: R")
    interest_rate_bond = input("What is your annual interest rate percentage: ")
    interest_rate_bond_strip = interest_rate_bond.strip("%")
    months = input("How many months will you be repaying the bond over: ")
    interest_rate_bond_monthly = (float(interest_rate_bond_strip) / 12)/100
    monthly_payments = (interest_rate_bond_monthly * float(present_value)) / (1 - (1 + interest_rate_bond_monthly)**(-int(months)))
    print(f"You will have monthly payments of R{monthly_payments:.2f}")

#else statement outputs an error message
else:
    print("You did not enter a valid option")
