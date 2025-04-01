import random

rule = 'What number is missing in the progression?'


def processing_game():
    first_number = random.randint(1, 10)
    the_number_for_progression = random.randint(1, 10)
    progression = []
    for i in range(10):
        progression.append(first_number)
        first_number += the_number_for_progression
    return progression, str(the_number_for_progression)