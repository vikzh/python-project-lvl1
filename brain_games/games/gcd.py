from random import randrange

TITLE = 'Find the greatest common divisor of given numbers.'


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
