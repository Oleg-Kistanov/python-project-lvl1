#!/usr/bin/env python3

import random


def parity_check():
    expression = random.randint(1, 15)

    if expression % 2 == 0:
        answer = "yes"
    else:
        answer = "no"

    return (answer, expression)
