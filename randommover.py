#!bin/python3
import random

input()
input()
input()
w = input()
directions = ['W', 'N', 'S', 'E']
while w != "QUIT":
    if w == "MOVE":
        print(random.choice(directions))
    w = input()