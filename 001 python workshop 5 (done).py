# Coding Challenge 1
# Name: Jorge Eduardo Dal Santo Ceatano
# Student No: 2038025

# A Simple and Compound Interest Calulator
import math
def print_intro():
    #prints intro
    print("Welcome to the Wolving compound interest calculator.\nThis program calculates your potential returns when you invest with us\n")


def get_input():
    #here we get the values the client wishes to calculate
    #we also already convert the years to its highest so 6.1 becomes 7 using the math.ceil
    amount_invest_value = float(input("How much would you like to invest? "))
    interest_rate_value = float(input("What is the interest rate on your account? "))
    years_invest_value = math.ceil(float(input("How long are you planning to invest (in years)? ")))
    return amount_invest_value, interest_rate_value, years_invest_value


def simple_interest(principal, rate, years):
    #here we convert the rate to a decimal value and then plug everything into the magical formula
    rate = rate / 100
    total_simple = principal * (1 + rate * years)
    return total_simple


def compound_interest(principal, rate, years):
    #since this specific bank has a fixed amount of compounds a year we make it a fixed number instead of gathering it from the input
    #then we convert rate to decimal and do the magical formula again and return the value from the formula
    compound_a_year = 4
    rate = rate / 100
    total_compound = principal * (1 + rate / compound_a_year) ** (compound_a_year * years)
    return total_compound


def print_simple_output(principal, rate, years, result):
    #if result isnt negative years we print it otherwise 0
    #here i learned 2 things, .format and {:.2f} which saved me from doing a for loop
    if result < 0: result = 0
    print("\n{} invested at {}% for {} years is £{:.2f}.".format(principal, rate, years, result))


def print_compounding_output(principal, rate, years, result):
    #same as above
    if result < 0: result = 0
    print("{} invested at {}% for {} years compounded 4 times per year is £{:.2f}.\n".format(principal, rate, years, result))


# ---------- Challenge Functions (Optional) ----------

def print_target_output(principal, rate, years):
    #same as above
    if years < 0: years = 0
    print("\n£{:.2f} invested at {}% will allow you to reach your savings target in {} years.\n".format(principal, rate, years))

def get_target_input():
    #input is gathered and returned as a tuple
    value = float(input("How much would you like to invest? "))
    rate = float(input("What is the interest rate on your account? "))
    goal = float(input("What is your savings goal? "))
    return value,rate,goal

def calculate_years_to_target(principal, rate, target):
    #decimal conversion then formula
    rate = rate / 100
    return math.ceil((math.log(principal/target)) / (4 * math.log(1 - rate / 4)))

# ---------- Main driver function ----------
# 1.	Print a welcome message explaining the purpose of the program.
# 2.	Prompt the user for the necessary inputs (see formulae and brief) and convert the values the user enters into suitable data types.
# 3.	Perform the simple and compound interest calculations.
# 4.	Print the results to the terminal in the format specified.
def main():
    while True: #forever loop
        print_intro() #print intro
        choice = input("Would you like to:\n1. Calculate simple and compound interest over time\n2. Calculate the amount of time required to hit a savings goal.\n") #aks which method of calculation should be used
        if choice == '1': #runs simple and compound functions
            a,b,c = get_input(choice) #separates tuple into separated variables
            simple_value = float(simple_interest(a,b,c))
            compound_value = float(compound_interest(a,b,c))
            print_simple_output(a,b,c,simple_value)
            print_compounding_output(a,b,c,compound_value)
        elif choice == '2':
            a,b,c = get_target_input()
            d = calculate_years_to_target(a,b,c)
            print_target_output(a,b,d)
        else: print("F")
# Program execution begins here
if __name__ == '__main__':
    main()
