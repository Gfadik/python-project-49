import prompt
import random
from brain_games.scripts import cli
from brain_games.scripts import logik


def true_or_false():
	cli.welcome_user()
	print(f'Answer "yes" if the number is even, otherwise answer "no".')
	i = 0
	while i < 3:
		i += 1
		number = random.randint(1,100)
		check_answer = number % 2
		if check_answer == 0:
			correct_answer = 'yes'
		else:
			correct_answer = 'no'
		logik.logik_in_game(number, correct_answer)
	cli.end()
true_or_false()
