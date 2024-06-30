import random


question = 'Find the greatest common divisor of given numbers.'


def create_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = str(number_1) + ' ' + str(number_2)
    counter = min(number_1, number_2)
    min_gcd = 1
    right_answer = min_gcd
    while counter > 0 and min_gcd == 1:
        if number_1 % counter == 0 and number_2 % counter == 0:
            right_answer = counter
        counter -= 1
    return expression, right_answer
