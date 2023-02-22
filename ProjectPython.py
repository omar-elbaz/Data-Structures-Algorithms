# DMV Test Project
# Create List of Correct Answers
answer_key = ['A\n','C\n','A\n','A\n','D\n',
'B\n','C\n','A\n','C\n','B\n',
'A\n','D\n','C\n','A\n','D\n',
'C\n','B\n','B\n','D\n','A\n',]


responses = []
student_answers = open('student_answers_project.txt','r')
for line in student_answers:
    answer = line
    responses.append(answer)


incorrect_questions = []
correct_answers = 0
incorrect_answers = 0
for i in range(len(responses)) :
    if responses [i] == answer_key [i]:
        correct_answers += 1
    else:
        incorrect_questions.append(i+1)
        incorrect_answers += 1
if correct_answers >= 15:
    result = "Congratulations you Passed!"
else:
    result = "Sorry you have Failed the exam"
print()
print(result)
if len(incorrect_questions)>0:
    print("You have answered the following questions incorrectly", incorrect_questions)
else:
    print('You answered all the questions correctly')


