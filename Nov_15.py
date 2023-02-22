# def main():
#     # Open a file named philosophers.txt.
#     outfile = open('philosophers.txt', 'w')
#     # Write the names of three philosphers
#     # to the file.
#     outfile.write('John Locke\n')
#     outfile.write('David Hume\n')
#     outfile.write('Edmund Burke\n')
#     # Close the file.
#     outfile.close()
# # Call the main function.
# main()



# def main():
#     # Open a file named philosophers.txt.
#     infile = open('philosophers.txt', 'r')
#     # Read the file's contents.
#     file_contents = infile.read()
#     # Close the file.
#     infile.close()
#     # Print the data that was read into
#     # memory.
#     print(file_contents)
# # Call the main function.
# main()


# Random 
# Number File Writer

# import random
# n = int(input("How Many Random Numbers do you want to generate? Enter a number:  "))
# numbers = open('randomint.txt','w')
# for i in range(n+1):
#     numbers.write(str(random.randint(1,500))+'\n')

# def main():
#     # Local variables
#     counter = 0
#     total = 0
#     number = 0    
#     # Open input file
#     inputFile = open('randomint.txt', 'r')
#     # Read numbers from the file while keeping count 
#     # and a running total
#     for line in inputFile:
#         number = int(line)
#         total += number
#         counter += 1
#     # Close the file
#     inputFile.close()
#     print('Total:', format(total, ','))
#     print(counter, 'numbers were read from the file.')
# # Call the main function.
# main()

# def main():
#     tv_file = open('runningtimes.txt', 'w')
#     n = int(input("How many videos did you take?  "))
#     print(n)
#     for i in range (n+1):
#         tv_file.write(input("Enter the running time of Video #" + i +': '))
    
#     # Close the file.
#     infile.close()
#     # Print the data that was read into
#     # memory.
#     print(file_contents)
# # Call the main function.
# main()

# This program gets employee data from the user and
# saves it as records in the employee.txt file.
# def main():
    
#     num_emps = int(input('How many employee records ' + \
#                          'do you want to create? '))
    
#     emp_file = open('employees.txt', 'w')
    
#     for count in range(1, num_emps + 1):
#         print('Enter data for employee #', count, sep='')
#         name = input('Name: ')
#         id_num = input('ID number: ')
#         dept = input('Department: ')
#         emp_file.write(name + '\n')
#         emp_file.write(id_num + '\n')
#         emp_file.write(dept + '\n')
#         print()
#     emp_file.close()
#     print('Employee records written to employees.txt.')
# main()

def main():
    student_answers = open('student_answers.txt','w')
    inputted_answers = ['A','C','A','A','D',
'B','C','A','C','B',
'A','D','C','A','D',
'C','B','B','D','A']
    for i in range (len(inputted_answers)):
        student_answers.write(inputted_answers[i])
        student_answers.write('\n')

main()


# list = [10,20,30,40,50]
# print(len(list))

# numbers = [1,2,3,4,5,6]