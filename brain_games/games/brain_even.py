from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(expression):
    return expression % 2 == 0


def create_round_data():
    expression = randint(1, 100)
    if is_even(expression):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = str(expression)
    return expression, right_answer
