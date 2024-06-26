import random

import prompt
from random import randint, choice


def check_random(random_number) -> bool:
    if random_number % 2 == 0:
        return True
    return False

def calculate_expression(number_1, number_2, operator) -> int:
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    return result


def calculations(game_type):
    if game_type == 'brain_even':
        random_number = randint(1, 100)
        check = check_random(random_number)
        if check is True:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        return str(random_number), right_answer
    if game_type == 'brain_calc':
        list_operators = ['+', '-', '*']
        operator = random.choice(list_operators)
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        expression = str(number_1) + operator + str(number_2)
        right_answer = calculate_expression(number_1, number_2, operator)
        return expression, right_answer


def game_question(game_type):
    if game_type == 'brain_even':
        game_question = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    if game_type == 'brain_calc':
        game_question = 'What is the result of the expression?'
    return game_question

def engine(game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    counter_for_right_answers = 0
    print(game_question(game_type))
    while counter_for_right_answers < 3:
        expression, right_answer = calculations(game_type)
        print(f'\n Question: {expression}.')
        player_answer = prompt.string('Your answer: ')
        if str(player_answer) == str(right_answer):
            print('Correct!')
            counter_for_right_answers += 1
    print(f'Congratulations, {name}')


def main(game_type):
    engine(game_type)