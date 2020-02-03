from brain_games.cli import welcome_user
from prompt import string

GAMES_TO_WIN = 3


def game(title, get_question_and_right_answer):
    name = welcome_user(title)
    wins = 0

    while wins < GAMES_TO_WIN:
        (question, right_answer) = get_question_and_right_answer()
        print('Question: {}'.format(question))
        user_answer = string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            wins += 1
        else:
            print('{} is wrong answer ;(. Correct answer was {}'
                  .format(user_answer, right_answer))
            print('Lets try again, {}!'.format(name))
            return

    print('Congratulations, {}'.format(name))
