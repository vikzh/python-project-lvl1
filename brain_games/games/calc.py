from random import choice
from random import randrange
from operator import add
from operator import sub
from operator import mul

TITLE = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def make_question_and_answer():
    random_range = 100
    random_operation_symbol, random_operation = choice(OPERATIONS)
    first_num = randrange(random_range)
    second_num = randrange(random_range)
    question = '{} {} {}'.format(first_num,
                                 random_operation_symbol,
                                 second_num)
    right_answer = str(random_operation(first_num, second_num))

    return question, right_answer
