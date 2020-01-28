from brain_games.scripts.game_engine import game
from random import randrange

TITLE = 'Answer "yes" if number even otherwise answer "no".'


def main():
    game(TITLE, make_question_and_answer)


def make_question_and_answer():
    question = randrange(100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer


if __name__ == '__main__':
    main()
