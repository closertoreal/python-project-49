#!/usr/bin/env python3


from brain_games import brain_interface
from brain_games.games.brain_prime import question, create_question


def main():
    brain_interface.main(question, create_question)


if __name__ == '__main__':
    main()
