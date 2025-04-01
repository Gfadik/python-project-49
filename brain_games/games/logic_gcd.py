import random
import math


rule = "Find the greatest common divisor of given numbers."

def processing_game():
    number_first = random.randint(1,100)
    number_second = random.randint(1, 100)
    question = f'{number_first}  {number_second}'
    correct_answer = math.gcd(number_first, number_second)
    return question,str(correct_answer)