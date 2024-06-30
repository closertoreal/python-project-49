import random


question = 'What number is missing in the progression?'


def create_question():
    progression = []
    list_length = random.randint(5, 10)
    progression_step = random.randint(1, 100)
    swap = random.randint(1, 100)
    progression.append(swap)
    item_to_remove = random.randint(1, list_length)
    while list_length >= 0:
        swap += progression_step
        progression.append(str(swap))
        list_length -= 1
    right_answer = progression[item_to_remove]
    progression[0] = str(progression[0])
    progression[item_to_remove] = '..'
    expression = ' '.join(progression)
    return expression, right_answer
