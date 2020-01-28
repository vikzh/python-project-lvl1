#!/usr/bin/env python3
from brain_games.scripts.game_engine import game
from random import randrange

TITLE = 'Find the greatest common divisor of given numbers.'


def main():
    game(TITLE, make_question_and_answer)


def make_question_and_answer():
    x = randrange(100)
    y = randrange(100)
    question = '{} {}'.format(x, y)
    right_answer = gcd(x, y)
    return question, str(right_answer)


def gcd(x, y):
    if y > x:
        return gcd(y, x)
    elif not y:
        return x
    return gcd(y, x % y)


if __name__ == '__main__':
    main()
