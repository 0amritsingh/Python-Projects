import random
import time

start = input('Press ENTER to START')
print('-' * 20)

questions = []
answers = []

for i in range(1,11):
    a = random.randint(1,11)
    o = random.choice(['+', '-', 'x', '/'])
    b = random.randint(1,11)
    question = f'{a} {o} {b}'
    questions.append(question)
    if o == '+':
        answers.append(float(a + b))
    if o == '-':
        answers.append(float(a - b))
    if o == 'x':
        answers.append(float(a * b))
    if o == '/':
        answers.append(round(float(a / b), 2))

initial = time.time() # time starts
i = 0
while i < 10:
    user_input = float(input(f'Problem #{i + 1}: {questions[i]} = '))
    if user_input == answers[i]:
        i = i + 1
final = time.time() # time ends

print('-' * 20)
print(f'You finised in {round(final - initial, 2)} seconds')
        