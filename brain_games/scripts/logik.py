import prompt


def logik_in_game(question, correct_answer):
        print(f'Question:{question}')
        users_answer = prompt.string('Your answer: ')
        if correct_answer == users_answer:
                print('Correct!')
        else:
                print(f"'{users_answer}' is wrong answer ;(. Correct answer was {correct_answer}")
                exit()
