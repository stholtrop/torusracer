#!bin/python3
import random

input()
input()
input()
w = input()
directions = ['W', 'N', 'S', 'E']
dir = random.choice(directions)
while w != "QUIT":
    if w == "MOVE":
        print(dir)
    w = input()