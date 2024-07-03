from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(expression):
    return (
        not (
            expression % 2 == 0 and expression != 2
            or expression % 3 == 0 and expression != 3
            or expression % 5 == 0 and expression != 5
        )
    )


def create_round_data():
    expression = randint(1, 100)
    if is_prime(expression):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = str(expression)
    return expression, right_answer
