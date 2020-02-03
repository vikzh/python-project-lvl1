from random import randrange

TITLE = 'What number is missing in the progression?'


def make_question_and_answer():
    progression_length = 10
    step = randrange(1, 10)
    start = randrange(100)
    progression_elements = list(range(
        start,
        start + progression_length * step,
        step))
    random_progression_index = randrange(len(progression_elements))
    right_answer = progression_elements[random_progression_index]
    progression_elements[random_progression_index] = '...'
    question = ' '.join(map(str, progression_elements))
    return question, str(right_answer)
