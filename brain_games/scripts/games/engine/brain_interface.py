import random
from random import randint
import prompt


def check_random(random_number, game_type) -> bool:
    match game_type:
        case 'brain_even':
            if random_number % 2 == 0:
                answer = 'yes'
            else:
                answer = 'no'
        case 'brain_prime':
            if random_number % 2 == 0 and random_number != 2:
                answer = 'no'
            elif random_number % 3 == 0 and random_number != 3:
                answer = 'no'
            elif random_number % 5 == 0 and random_number != 5:
                answer = 'no'
            else:
                answer = 'yes'
    return answer


def calculate_expression(number_1, number_2, operator) -> int:
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    return result


def calculations(game_type):
    match game_type:
        case 'brain_even' | 'brain_prime':
            random_number = randint(1, 100)
            right_answer = check_random(random_number, game_type)
            expression = str(random_number)
        case 'brain_calc':
            list_operators = ['+', '-', '*']
            operator = random.choice(list_operators)
            number_1 = random.randint(1, 100)
            number_2 = random.randint(1, 100)
            expression = str(number_1) + operator + str(number_2)
            right_answer = calculate_expression(number_1, number_2, operator)
        case 'brain_gcd':
            number_1 = random.randint(1, 100)
            number_2 = random.randint(1, 100)
            expression = str(number_1) + ' ' + str(number_2)
            counter = min(number_1, number_2)
            right_answer = 0
            while counter > 0 and right_answer == 0:
                if number_1 % counter == 0 and number_2 % counter == 0:
                    right_answer = counter
                counter -= 1
        case 'brain_progression':
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


def game_question(game_type):
    match game_type:
        case 'brain_even':
            game_question = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
        case 'brain_calc':
            game_question = 'What is the result of the expression?'
        case 'brain_gcd':
            game_question = 'Find the greatest common divisor of given numbers.'
        case 'brain_progression':
            game_question = 'What number is missing in the progression?'
        case 'brain_prime':
            game_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return game_question


def engine(game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    counter_for_right_answers = 0
    print(game_question(game_type))
    while counter_for_right_answers < 3:
        expression, right_answer = calculations(game_type)
        print(f'\nQuestion: {expression}.')
        player_answer = prompt.string('Your answer: ')
        if str(player_answer) == str(right_answer):
            print('Correct!')
            counter_for_right_answers += 1
        else:
            print(f'{str(player_answer)} is wrong answer ;(. Correct answer was {str(right_answer)}.'
            f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')


def main(game_type):
    engine(game_type)
