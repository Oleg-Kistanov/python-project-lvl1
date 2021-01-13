#!/usr/bin/env python3

import random
from brain_games import cli


def parity_check():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    questions = 3

    while questions >= 0:
        number = random.randint(1, 15)
        answers = ["yes", "no"]
        if questions == 0:
            print(f"Congratulations, {name}!")
            break
        print("Question: " + str(number))
        user_input = input("Your answer: ")
        if number % 2 == 0 and user_input.lower() == answers[0] or \
                number % 2 != 0 and user_input.lower() == answers[1]:
            print("Correct!")
            questions -= 1
            continue
        if number % 2 == 0 and user_input.lower() == answers[1] or \
                number % 2 == 0 and user_input.lower() not in answers:
            print(f"'{user_input}' is wrong answer"
                  f" ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
            break
        else:
            print(f"'{user_input}' is wrong answer"
                  f" ;(. Correct answer was 'no'. \nLet's try again, {name}!")
            break
