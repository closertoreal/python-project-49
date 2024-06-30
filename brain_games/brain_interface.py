import prompt


def run_game(game_question, create_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    counter_for_right_answers = 0
    print(game_question)
    number_of_rounds = 3
    while counter_for_right_answers < number_of_rounds:
        expression, right_answer = create_question()
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


def main(game_question, create_question):
    run_game(game_question, create_question)
