#!/usr/bin/env python3


from brain_games import brain_interface
from brain_games.games import brain_even


def main():
    brain_interface.main(brain_even.question, brain_even.create_question)


main()