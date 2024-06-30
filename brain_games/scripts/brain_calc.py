#!/usr/bin/env python3


from brain_games import brain_interface
from brain_games.games import brain_calc


def main():
    brain_interface.main(brain_calc.question, brain_calc.create_question)


if __name__ == '__main__':
    main()
