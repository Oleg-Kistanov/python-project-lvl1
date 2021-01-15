#!/usr/bin/env python3

def check_answer(game, name):
    questions = 3

    while questions >= 0:
        if questions == 0:
            print(f"Congratulations, {name}!")
            break

        answer, expression = game()
        print(f"Question: {expression}")
        user_input = input("Your answer: ")

        if user_input == answer:
            print("Correct!")
            questions -= 1
            continue
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'. \nLet's try again, {name}! ")
            break
