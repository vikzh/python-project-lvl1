from brain_games.scripts.game_engine import game
from random import randrange


def main():
    game(make_question_and_answer)


def make_question_and_answer():
    progression_length = 10
    step = randrange(1, 10)
    start = randrange(100)
    progression_elements = generate_progression(start=start,
                                                step=step,
                                                length=progression_length)
    random_progression_index = randrange(len(progression_elements))
    right_answer = progression_elements[random_progression_index]
    progression_elements[random_progression_index] = '...'
    question = ' '.join(map(str, progression_elements))
    return question, str(right_answer)


def generate_progression(start, step, length):
    list_ = [start]
    for i in range(length - 1):
        list_.append(list_[-1] + step)
    return list_


if __name__ == '__main__':
    main()
