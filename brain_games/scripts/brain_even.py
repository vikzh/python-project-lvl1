from brain_games.cli import welcome_user
from brain_games.scripts.game_engine import game
from random import randrange


def main():
    game(make_question_and_answer)


def make_question_and_answer():
    question = randrange(100)
    right_answer = 'yes' if question % 2 is 0 else 'no'
    return question, right_answer


if __name__ == '__main__':
    main()
