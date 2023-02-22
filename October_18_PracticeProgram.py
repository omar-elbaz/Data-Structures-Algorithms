# October 18th Practice Programming (Omar Elbaz)

#"Calculating the factorial of a Number"

print('Let us calculate a factorial of a given number')
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i   
print("The factorial of",num,"is",factorial)   


# Calories Burned

print("Minutes",'\t''Calories Burned')
print('--------------')
for m in range (10,31, 5):
    calories = m * 4.2
    print(m, '\t', calories)

# Celsius to Farenheit
print("Celsius",'\t''Farenheit')
print('--------------')

for C in range (0,21, 5):
    F = (9/5)*C + 32
    print(C,'\t',F)


# Chris Auto Store
print ("Hello, let us calculate your pay")
Rate = 10
Hrs = int(input("How many Hours did you work? "))
LessHrs = Rate * Hrs
Normal_Pay = Rate * 40
Overtime = Rate * (1.5) * (Hrs-40)
if Hrs>40:
    pay = Overtime +Normal_Pay
    print("This week you will make $",pay)
elif  Hrs <= 40:
    print(LessHrs)


# Scholarship In Rutgers
print('Hello, Let us see if you qualify for the Rutgers Scholarship')
minnimum_years_in_school = 2
minnimum_gpa = 3.5

years = float(input('How many years have you been in school?'))
gpa = float(input('What is your gpa?'))

if years >= minnimum_years_in_school:
    if gpa >= minnimum_gpa:
        print('You qualify for the Rutgers Scholarship')
    else:
        print("Your gpa is not high enough, you need at least a 3.5 gpa")
else:
    print('You have not been in school long enough, you must be a student for at least 2 years')
