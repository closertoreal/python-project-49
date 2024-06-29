#!/usr/bin/env python3


from brain_games import brain_interface
from random import randint

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


def main():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    expression, right_answer = create_question()
    brain_interface.main(question, expression, right_answer)


if __name__ == '__main__':
    main()
