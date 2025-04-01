import random
import math


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def processing_game():
    question = random.randint(1,100)
    prime_number_check = math.gcd(question)
    if prime_number_check == question:
        correct_answer = yes
    else:
        correct_answer = no
    return question, correct_answer