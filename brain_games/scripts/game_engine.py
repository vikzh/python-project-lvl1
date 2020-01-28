from brain_games.cli import welcome_user
from prompt import string


def game(title, get_question_and_right_answer):
    games_to_win = 3
    name = welcome_user(title)
    wins = 0

    while wins < games_to_win:
        (question, right_answer) = get_question_and_right_answer()
        user_answer = string('Question: {}'.format(question))
        if user_answer == right_answer:
            print('Correct!')
            wins += 1
        else:
            print('{} is wrong answer ;(. Correct answer was {}'
                  .format(user_answer, right_answer))
            print('Lets try again, {}!'.format(name))
            return

    print('Congratulations, {}'.format(name))
