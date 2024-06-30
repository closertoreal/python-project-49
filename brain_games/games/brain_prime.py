from random import randint

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_answer(expression):
    if expression % 2 == 0 and expression != 2:
        answer = 'no'
    elif expression % 3 == 0 and expression != 3:
        answer = 'no'
    elif expression % 5 == 0 and expression != 5:
        answer = 'no'
    else:
        answer = 'yes'
    return answer


def create_question():
    expression = randint(1, 100)
    right_answer = calculate_answer(expression)
    expression = str(expression)
    return expression, right_answer
