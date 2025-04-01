import math
import random

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def processing_game():
    question_number = random.randint(1, 100)
    i = 2
    while i <= math.sqrt(question_number):
        checking_the_number = question_number % i
        if checking_the_number == 0:
            correct_answer = 'no'
            return question_number, correct_answer
        i += 1
    correct_answer = 'yes'
    return question_number, correct_answer