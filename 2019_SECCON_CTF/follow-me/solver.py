#!/usr/bin/env python3

import re
import random
import subprocess
import shlex


# Speed up random() by using a pseudo-random generator
random.seed(random.random())

# Formula extracted from previous step
formula = open('formula.txt', 'r').read().strip()


# Run a guess and get its fitness
def run(xxx):
    argv = shlex.split('./calc_8e4bdd821b86bebbfa6c5191bfddd40dbb120916')
    argv.append(xxx)
    p = subprocess.run(argv, env={
        'LD_PRELOAD': '/usr/lib/libpyqbdi.so',
        'PYQBDI_TOOL': './tracer.py',
        }, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return int(re.search(b'OUT (\d+)', p.stdout).group(1))


# Tokenize the formula (X == digit)
n = len(formula.split('X')) - 1
tokens = formula.split('X')

guess = [0] * n
score = 1000000

# Start the guessing game :)
while score > 0:
    new = guess[:]

    # Randomly modify the best guess
    for i in range(random.randint(1, 10)):
        new[random.randint(0, n-1)] = random.choice('1234567890')
    
    # Reconstruct a formula from the tokens
    s = ''
    for a, b in zip(tokens, new):
        s += a + str(b)
    s += tokens[-1]
    assert len(s) == len(formula)

    # Update the score and print the current best guess
    new_score = run(s)
    if new_score < score:
        print(score, s)
        score = new_score
        guess = new


