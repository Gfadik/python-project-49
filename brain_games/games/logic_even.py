import random

rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def processing_game():
	question = random.randint(1, 100)
	check_answer = question % 2
	if check_answer == 0:
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	return question, correct_answer
