#!/usr/bin/env python3


import prompt
from random import randint
from typing import Tuple


def check_random(random_number):
    if random_number % 2 == 0:
        return True
    return False


def interface() -> Tuple[str, str]:
    random_number = randint(1, 100)
    check = check_random(random_number)
    if check is True:
        answer = 'yes'
    else:
        answer = 'no'
    return str(random_number), answer


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    counter_for_right_answers = 0
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    while counter_for_right_answers < 3:
        random_number, text_answer = interface()
        print(f'\n Question: {random_number}.')
        player_answer = prompt.string('Your answer: ')
        if player_answer == text_answer:
            print('Correct!')
            counter_for_right_answers += 1
        else:
            print('Incorrect!')
    print(f'Congratulations, {name}')


welcome_user()
