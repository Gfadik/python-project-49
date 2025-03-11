import prompt
from game import brain_even


def begin():
	print('Welcome to the Brain Games!')


def main():
	begin()
	users_choose = prompt.integer('''Choose the game...
1.brain even
2.brain calc
''')
	if users_choose == 1:
        	game.brain_even.true_or_false()
	else:
		game.brain_calc.calc_game()

if __name__ == '__main__':
	main()
