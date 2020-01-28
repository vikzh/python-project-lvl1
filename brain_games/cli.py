import prompt


def welcome_user(title):
    print('Welcome to Brain Games!')
    print(title + '\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
