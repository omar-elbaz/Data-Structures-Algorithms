# This program displays step-by-step instructions
# for disassembling an Acme dryer.
# The main function performs the program's main logic.
def main():
    # Display the start-up message.
    startup_message()
    input('Press Enter to see Step 1.')
    # Display step 1.
    step1()
    input('Press Enter to see Step 2.')
    # Display step 2.
    step2()
    input('Press Enter to see Step 3.')
    # Display step 3.
    step3()
    input('Press Enter to see Step 4.')
    # Display step 4.
    step4()
# The startup_message function displays the
# program's initial message on the screen.
def startup_message():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer.')
    print('There are 4 steps in the process.')
    print()
# The step1 function displays the instructions
# for step 1.
def step1():
    print('Step 1: Unplug the dryer and')
    print('move it away from the wall.')
    print()
# The step2 function displays the instructions
# for step 2.
def step2():
    print('Step 2: Remove the six screws')
    print('from the back of the dryer.')
    print()
# The step3 function displays the instructions
# for step 3.
def step3():
    print('Step 3: Remove the back panel')
    print('from the dryer.')
    print()
# The step4 function displays the instructions
# for step 4.
def step4():
    print('Step 4: Pull the top of the')
    print('dryer straight up.')
# Call the main function to begin the program.
main()

def definition():
    print( "The definition of programming is:")
    print('The process or activity of writing computer programs.')


definition()


# Find Double
def find_double(): 
    print("Enter a number, I will tell you its double")
    value = int(input())
    result = value * 2 
    print(result)
# Call the  function. 
find_double()

def main():
    intro()
    cups_needed = int(input('Enter the number of cups: ')) 
    cups_to_ounces(cups_needed)
def intro():
    print()
    print('This program converts measurements') 
    print('in cups to fluid ounces. For your') 
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to', ounces, 'ounces.')
    print()

main()

# Automobile Costs

def intro_message():
    print()
    print("Welcome!") 
    print("I will help you calculate your automobile expenses")
    print()

print("Lets Calculate your monthly expenses" )

def calculate_costs():
    Loan = float(input('Enter monthly cost of Loan  '))
    Insurance = float(input('Enter monthly cost of Insurance  '))
    Gas = float(input('Enter monthly cost of Gas  '))
    Oil = float(input('Enter monthly cost of Oil  '))
    Tires = float(input('Enter monthly cost of Tires  '))
    Maint = float(input('Enter monthly cost of Maintenance  '))
    Total_Expense = Loan + Insurance + Gas + Oil + Tires + Maint 
    print()
    print("Your Monthly Automobile expenses are,", Total_Expense) 

    print()
    print("Now lets calculate your total annual expenses")
    Annual_Cost =  Total_Expense *12
    print()
    print("For reference the Annual expense is the monthly expense multiplied by 12" )
    print("Your Aunnual Automobile expenses are,", Annual_Cost) 
    print()





# def calculate_annual_Cost():

#     Annual_Cost =  Total_Expense *12
#     print("Your Aunnual Automobile expenses are,", Annual_Cost) 


intro_message()
calculate_costs()


