import game
import random

class Program:
    def __init__(self, height, width, number_of_players, player_number, start_positions):
        self.game = game.Game(height, width, start_positions)
        self.nop = number_of_players
        self.pn = player_number

    def update(self, player, move):
        self.game.move_player(player, move)

    def get_move(self):
        MOVES = list(game.MOVES)
        random.shuffle(MOVES)
        for i in MOVES:
            move = i
            self.game.move_player(self.pn, i)
            if self.game.alive[self.pn]:
                break
            self.game.undo_move()
        return move