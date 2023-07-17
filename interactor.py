import sys, game, time

class Player:
    def __init__(self, file, height, width, number_of_players, player_number, start_postitions):
        module = __import__(file)
        self.program = module.Program(height, width, number_of_players, player_number, start_postitions)

    def update(self, player_number, move):
        self.program.update(player_number, move)

    def get_move(self):
        return self.program.get_move()

width, height, number_of_players = 10, 10, 2
start_positions = ((0, 0), (5, 5))

g = game.Game(height, width, start_positions)
players = []

for i in range(len(sys.argv) - 1):
    players.append(Player(sys.argv[i + 1], height, width, number_of_players, i, start_positions))
f = open("record.txt", "w")

g = game.Game()

f.write("x, y, number of players: 100 100 2\n")
f.write("starting positions: 0 0 50 50\n")

# Game is played by asking current player to move
while not g.is_done():
    for i, p in enumerate(players):

        # Check if current player is still in the game
        if not g.alive[i]:
            continue
        
        # Get move of current player
        move = p.get_move() 

        # Communicate move to other players
        for j, q in enumerate(players):
            if i == j or not g.alive[j]: continue
            q.update(i, move)
        

        # Update logs
        f.write(f"Player {i} : {move}\n")
        result = g.move_player(i, move)
        if result: 
            f.write(f"Player {i} died.\n")
        if g.is_done():
            break

f.write(f"The winner is player {g.get_winner()}.\n")
f.write(g.get_board())
f.close()
