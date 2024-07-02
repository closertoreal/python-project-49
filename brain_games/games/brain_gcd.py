import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def calculate_answer(number_1, number_2):
    counter = min(number_1, number_2)
    min_gcd = 1
    right_answer = min_gcd
    while counter > 0 and min_gcd == 1:
        if number_1 % counter == 0 and number_2 % counter == 0:
            right_answer = counter
            return right_answer
        counter -= 1


def create_round_data():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = str(number_1) + ' ' + str(number_2)
    right_answer = calculate_answer(number_1, number_2)
    return expression, right_answer
