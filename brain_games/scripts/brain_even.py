import random

import prompt


def true_or_false():
	user_name = prompt.string('Welcome to the Brain Games!\nMay I have your name?\n')
	print(f'Hello, {user_name}!')
	print('Answer "yes" if the number is even, otherwise answer "no".')
	i = 0
	while i < 3:
		i += 1
		random_number = random.randint(1, 100)
		print(f'Question: {random_number}')
		answer = prompt.string('Your answer: ')
		check_for_parity = random_number % 2
		if check_for_parity == 0 and answer == 'yes' or check_for_parity == 1 and answer == 'no':
			print('Correct!')
			continue
		else:
			if answer == 'yes':
				print("'yes' is wrong answer ;(. Correct answer was 'no'.")
				print(f"Let's try again, {user_name}")
				exit()
			else:
				print("'no' is wrong answer ;(. Correct answer was 'yes'.")
				print(f"Let's try again, {user_name}")
				exit()
	print('Congratulations,{user_name}!')


true_or_false()
