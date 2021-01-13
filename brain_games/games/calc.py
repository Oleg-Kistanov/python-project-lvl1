import prompt
import random
import operator
from brain_games import cli


def welcome_user():
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    return name


def calculator():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print('What is the result of the expression?')

    questions = 3

    while questions >= 0:
        number_1 = random.randint(1, 25)
        number_2 = random.randint(1, 25)
        operations = {"+": operator.add,
                      "-": operator.sub,
                      "*": operator.mul}
        op = random.choice(list(operations.keys()))
        answer = operations[op](number_1, number_2)
        if questions == 0:
            print(f"Congratulations, {name}!")
            break
        print(f"Question: {number_1} {op} {number_2}")
        user_input = input("Your answer: ")
        if user_input == str(answer):
            print("Correct!")
            questions -= 1
            continue
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer "
                  f"was '{answer}'. \nLet's try again, {name}!")
            break
