from subprocess import Popen, PIPE
import sys
import game
import time

p1 = Popen(["python3", "-u", sys.argv[1]], stdin=PIPE, stdout=PIPE, bufsize=1, text=True)
p2 = Popen(["python3", "-u", sys.argv[2]], stdin=PIPE, stdout=PIPE, bufsize=1, text=True)

players = [p1, p2]

f = open("record.txt", "w")

g = game.Game()

# setup: first print board dimensions and number of players, then print your player id. Next up all positions of the players in order
for i, p in enumerate(players):
    p.stdin.write("100 100 2\n")
    p.stdin.write(f"{i}\n")
    p.stdin.write("0 0 50 50\n")

f.write("100 100 2\n")
f.write("0 0 50 50\n")

# Game is played by asking current player to move
while not g.is_done():
    for i, p in enumerate(players):
        print(i)
        if not g.alive[i]:
            continue
        p.stdin.write("MOVE\n")
        p.stdin.flush()
        move = p.stdout.readline()[:-1]
        for j, q in enumerate(players):
            if i == j: continue
            q.stdin.write(f"{i} {move}")
        f.write(f"{i} {move}")
        result = g.move_player(i, move)
        if result: 
            p.communicate("QUIT\n")
            f.write(f"Player {i} died.\n")
        if g.is_done():
            break
players[g.get_winner()].communicate("QUIT\n")
f.write(f"The winner is player {g.get_winner()}.")
f.close()
