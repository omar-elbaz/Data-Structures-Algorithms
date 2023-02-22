#Random Number Guessing Game

import random

# def main():
#     print()
#     print("I have generated a number between 0 and 100, try and guess it. Good Luck!")
#     x = random.randint(0,100)
#     y = int(input("Enter a Number between 0 and 100: "))
#     correct_guesses = 0
#     guesses = 0
#     keep_going = "y"
#     while keep_going == "y":
#         if y > x:
#             y = int(input("Too high try again: "))
#             guesses += 1
            
#         if y < x:
#             y = int(input("Too Low try again: "))
#             guesses += 1

#         if y == x:
#             print("Congratulations you guessed the right number")
#             correct_guesses += 1
#             guesses +=1
#             print("It took you", guesses, "guesses to reach the correct answer")
#             print()
#             print("You have made", correct_guesses, "correct guesses")
#             guesses = 0

#             x = random.randint(0,100)
#             print()
#             print( "A new number has been generated")
#             print()
#             y = int(input("Enter a Number between 0 and 100: "))
        
 
# main()
            
def main():
    array = []
    for i in range (6):
        x = random.randint(0,100)
        array.append(x)
    print (array)

main()
            
