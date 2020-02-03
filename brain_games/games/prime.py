from random import randrange
from math import sqrt

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question_and_answer():
    question = randrange(100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True
