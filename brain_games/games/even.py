from random import randrange

TITLE = 'Answer "yes" if number even otherwise answer "no".'


def make_question_and_answer():
    question = randrange(100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer
