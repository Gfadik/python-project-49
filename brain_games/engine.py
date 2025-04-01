import prompt


def engine_in_games(games):
    name = prompt.string('What is your name? ')
    print(f'Hello, {name}')
    print(f'{games.rule}')
    i = 1
    for i in range(3):
        task, correct_answer = games.processing_game()
        print(f'Question:{task}')
        users_answer = prompt.string('Your answer: ')
        if correct_answer == users_answer:
            print('Correct!')
        else:
            print(f"'{users_answer}' is wrong answer ;(. "
                  f"Correct answer was {correct_answer}")
            print(f'Lets try again, {users_answer}!')
            exit()
        print(f'Congratulations, {name}!')

