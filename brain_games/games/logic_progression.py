import random


rule = 'What number is missing in the progression?'

def processing_game():
    first_number = random.randint(1, 10)
    the_number_for_progression = random.randint(1, 10)
    random_index_progression = random.randint(0,9)
    progression = []
    for i in range(10):
        progression.append(first_number)
        first_number += the_number_for_progression
    correct_answer = progression[random_index_progression]
    progression[random_index_progression] = '..'
    question = ', '.join(map(str,progression))
    return question, str(correct_answer)