import random


QUESTION = 'What number is missing in the progression?'


def create_sequence(list_length, progression_step, start, item_to_remove):
    progression = []
    while list_length >= 0:
        start += progression_step
        progression.append(str(start))
        list_length -= 1
    right_answer = progression[item_to_remove]
    progression[0] = str(progression[0])
    progression[item_to_remove] = '..'
    expression = ' '.join(progression)
    return expression, right_answer


def create_round_data():
    list_length = random.randint(5, 10)
    progression_step = random.randint(1, 100)
    start = random.randint(1, 100)
    item_to_remove = random.randint(1, list_length)
    return create_sequence(list_length, progression_step, start, item_to_remove)
