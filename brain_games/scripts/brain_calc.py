#!/usr/bin/env python3
from brain_games.scripts.game_engine import game
from random import choice
from random import randrange
from operator import add
from operator import sub
from operator import mul

TITLE = 'What is the result of the expression?'


def main():
    game(TITLE, make_question_and_answer)


def make_question_and_answer():
    random_range = 100
    operations = [('+', add), ('-', sub), ('*', mul)]
    random_operation_symbol, random_operation = choice(operations)
    first_num = randrange(random_range)
    second_num = randrange(random_range)
    question = '{} {} {}'.format(first_num, random_operation_symbol, second_num)
    right_answer = str(random_operation(first_num, second_num))

    return question, right_answer
