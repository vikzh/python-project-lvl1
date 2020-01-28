from brain_games.scripts.game_engine import game
from random import choice
from random import randrange

TITLE = 'What is the result of the expression?'


def main():
    game(TITLE, make_question_and_answer)


def make_question_and_answer():
    random_range = 100
    operations = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
        '*': lambda num1, num2: num1 * num2
    }

    random_operation = choice(list(operations.keys()))
    first_num = randrange(random_range)
    second_num = randrange(random_range)
    question = '{} {} {}'.format(first_num, random_operation, second_num)
    right_answer = str(operations[random_operation](first_num, second_num))

    return question, right_answer
