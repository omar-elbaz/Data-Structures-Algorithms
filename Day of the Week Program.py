 # Omar Elbaz - Computers and Programming 
# Welcome!
# Program for Days of the Week
print( )

print("Welcome!, Enter a number and I will tell you the corresponding day of the week.")

print( )

val = int(input("Enter Number from 1-7! "))

print( )

if val == 1:
    day = "SUNDAY"
    print("The day of the week is",day)
elif val == 2:
    day = "MONDAY"
    print("The day of the week is",day)
elif val == 3:
    day = "TUESDAY"
    print("The day of the week is",day)
elif val == 4:
    day = "WEDNESDAY"
    print("The day of the week is",day)
elif val == 5:
    day = "THURSDAY"
    print("The day of the week is",day)
elif val == 6:
    day = "FRIDAY"
    print("The day of the week is",day)
elif val == 7:
    day = "SATURDAY"
    print("The day of the week is",day)
     
else:
    print("ERROR!!! Day doesn't exist.")

print( )
