#!/usr/bin/env python3


from brain_games import brain_interface
from brain_games.games import brain_gcd


def main():
    brain_interface.main(brain_gcd.question, brain_gcd.create_question)


if __name__ == '__main__':
    main()
