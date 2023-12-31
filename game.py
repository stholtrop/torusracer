MOVES = ("N", "S", "E", "W")

class Game:
    def __init__(self, height=10, width=10, player_positions=[[0, 0], [5, 5]]):
        self.board = [[0 for i in range(width)] for j in range(height)]
        self.height = height
        self.width = width
        self.player_positions = list(map(list, player_positions))
        self.alive = [True for i in range(len(player_positions))]
        self.move_list = []
        for y, x in player_positions:
            self.board[y][x] = 1

    '''
        function move_player
            player - index of the moving player
            direction - movement direction of player specified by N, E, S or W.
    '''
    def move_player(self, player, direction):
        if direction == 'N':
            self.player_positions[player][0] -= 1
        if direction == 'S':
            self.player_positions[player][0] += 1
        if direction == 'E':
            self.player_positions[player][1] += 1
        if direction == 'W':
            self.player_positions[player][1] -= 1
        
        self.player_positions[player][0] %= self.height
        self.player_positions[player][1] %= self.width
        
        x, y = self.player_positions[player][0], self.player_positions[player][1]

        result = self.board[x][y]
        self.board[x][y] = 1

        self.alive[player] = not result

        self.move_list.append((player, direction, result))

        return result
    
    def undo_move(self):
        player, direction, prev_state = self.move_list.pop()
        x, y = self.player_positions[player][0], self.player_positions[player][1]

        self.board[x][y] = prev_state
        
        if direction == 'N':
            self.player_positions[player][0] += 1
        if direction == 'S':
            self.player_positions[player][0] -= 1
        if direction == 'E':
            self.player_positions[player][1] -= 1
        if direction == 'W':
            self.player_positions[player][1] += 1
        
        self.player_positions[player][0] %= self.height
        self.player_positions[player][1] %= self.width

        self.alive[player] = True
    
    def is_done(self):
        return sum(self.alive) <= 1
    
    def get_winner(self):
        return self.alive.index(True)
    
    def get_board(self):
        return "\n".join("".join(map(str, l)) for l in self.board)+"\n"
    
    def print_board(self):
        print(self.get_board())