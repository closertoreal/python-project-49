import random


QUESTION = 'What is the result of the expression?'


def calculate_answer(number_1, number_2, operator):
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    elif operator == '*':
        answer = number_1 * number_2
    return answer


def create_round_data():
    list_operators = ['+', '-', '*']
    operator = random.choice(list_operators)
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = str(number_1) + ' ' + operator + ' ' + str(number_2)
    right_answer = calculate_answer(number_1, number_2, operator)
    return expression, right_answer
