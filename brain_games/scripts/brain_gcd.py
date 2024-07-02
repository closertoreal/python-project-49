#!/usr/bin/env python3


from brain_games.brain_interface import run_game
from brain_games.games.brain_gcd import QUESTION, create_round_data


def main():
    run_game(QUESTION, create_round_data)


if __name__ == '__main__':
    main()
