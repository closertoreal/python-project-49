import random
from random import randint
import prompt
from brain_games.games import brain_even


def engine(game_question, expression, right_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    counter_for_right_answers = 0
    print(game_question)
    while counter_for_right_answers < 3:
        expression, right_answer = brain_even.create_question()
        print(f'\nQuestion: {expression}.')
        player_answer = prompt.string('Your answer: ')
        if str(player_answer) == str(right_answer):
            print('Correct!')
            counter_for_right_answers += 1
        else:
            print(f"{str(player_answer)} is wrong answer ;(. "
                  f"Correct answer was {str(right_answer)}. "
                  f"Let\'s try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main(game_question, expression, right_answer):
    engine(game_question, expression, right_answer)
