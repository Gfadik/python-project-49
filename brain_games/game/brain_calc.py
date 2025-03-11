import random
from brain_games.scripts import cli
from brain_games.scripts import logik


def culc_game():
	cli.welcome_user()
	print(f'What is the result of the expression?')
	i = 0
	while i < 3:
		i += 1
		number_first = random.randint(1,100)
		number_second = random.randint(1,100)
		action = ['+','-','*']
		random_action = random.choice(action)
		question = f'{number_first} {random_action} {number_second}'
		if random_action == '+':
			correct_answer = number_first + number_second
		elif random_action == '-':
			correct_answer = number_first - number_second
		else:
			correct_answer = number_first * number_second
		prepared_correct_answer = str(correct_answer)
		logik.logik_in_game(question, prepared_correct_answer)
	cli.end()
culc_game()
