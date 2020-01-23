from brain_games.cli import welcome_user
from prompt import string
from random import randrange


def main():
    name = welcome_user()
    wins = 0

    while wins < 3:
        question = randrange(100)
        answer = string('Question: {}'.format(question))
        right_answer = 'yes' if question % 2 is 0 else 'no'
        if answer == right_answer:
            print('Correct!')
            wins += 1
        else:
            print('{} is wrong answer ;(. Correct answer was {}'.format(answer, right_answer))
            print('Lets try again, {}!'.format(name))
            return

    print('Congratulations, {}'.format(name))


if __name__ == '__main__':
    main()
