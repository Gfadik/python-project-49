import random

rule = 'What is the result of the expression?'


def processing_game():
    number_first = random.randint(1, 100)
    number_second = random.randint(1, 100)
    action = ['+', '-', '*']
    random_action = random.choice(action)
    question = f'{number_first} {random_action} {number_second}'
    if random_action == '+':
        correct_answer = number_first + number_second
    elif random_action == '-':
        correct_answer = number_first - number_second
    else:
        correct_answer = number_first * number_second
    return question, str(correct_answer)