from random import randint

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_answer(expression):
    if expression % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def create_question():
    expression = randint(1, 100)
    right_answer = calculate_answer(expression)
    expression = str(expression)
    return expression, right_answer




