


# import random
# def main():
#     # Get a random number.
#     number = random.randint(1, 10)
#     # Display the number.
#     print('The number is', number)
# # Call the main function.
# main()


# practice program


# DISCOUNT_PERCENTAGE = 0.20
# Commission = .10

# def main():
#     reg_price = get_regular_price()
#     sale_price = reg_price - discount(reg_price) -  commissionrate(reg_price)
#     print('The sale price is $', format(sale_price, ',.2f'), sep='')
# def get_regular_price():
#     price = float(input("Enter the item's regular price: "))
#     return price
# def discount(price):
#     return price * DISCOUNT_PERCENTAGE
# def commissionrate(price):
#     return price * Commission
# main()





# # trigfunctions

# import math

# def trig_functions(angle):
#     sin = (math.sin(math.radians(angle)))
#     cos = (math.cos(math.radians(angle)))
#     tan = (math.tan(math.radians(angle)))
#     print(sin)
#     print(cos)
#     print(tan)

# trig_functions(90)

# def trig_functions(angle):
#     sin = (math.sin(angle))
#     cos = (math.cos(angle))
#     tan = (math.tan(angle))
#     print(sin)
#     print(cos)
#     print(tan)

# trig_functions(90)


# Random Odd Even

import random


def main():
    even = 0
    odd = 0
    for i in range (100):
        number = random.randint(1,1001)
        if number % 2 == 1:
            odd +=1
        if number % 2 == 0:
            even +=1
    print( "There are", odd , "odd numbers" )
    print( "There are", even , "even numbers" )

            
main()

# from collections import Counter
# c = Counter(list1)


