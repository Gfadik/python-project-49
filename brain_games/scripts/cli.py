import prompt
def welcome_user():
        global name
        name = prompt.string('What is your name? ')
        print(f'Hello, {name}')
def end():
        print(f'Congratulations, {name}!')