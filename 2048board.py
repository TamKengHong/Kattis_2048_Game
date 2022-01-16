arr, d = [list(map(int, input().split())) for _ in range(4)], int(input())

class Board:
    def __init__(self, board_state): self.board_state = board_state

    def move(self, start_pos, end_pos):
        piece = self.board_state[start_pos[0]][start_pos[1]]
        piece.row, piece.col = end_pos[0], end_pos[1]
        self.board_state[end_pos[0]][end_pos[1]], self.board_state[start_pos[0]][start_pos[1]] = piece, None

    def shift_all_tiles(self, direction): # works
        for i in range(4):
            for j in range(4):
                dict1 = {(0, -1): self.board_state[i][j], (-1, 0): self.board_state[j][i],
                         (0, 1): self.board_state[i][3 - j], (1, 0): self.board_state[3 - j][i]}
                if dict1[direction] is not None: dict1[direction].shift(direction, self)

class Tile:
    def __init__(self, number): self.number, self.row, self.col, self.merged = number, None, None, False

    def shift(self, direction, board):
        while self.row + direction[0] in range(4) and self.col + direction[1] in range(4):
            new_pos = (self.row + direction[0], self.col + direction[1])
            tile = board.board_state[new_pos[0]][new_pos[1]]
            if tile is None: 
                board.move((self.row, self.col), new_pos)
            else:
                if tile.number == self.number and tile.merged == False:
                    self.number, self.merged = self.number * 2, True; board.move((self.row, self.col), new_pos)
                break

def board_state_converter(arr):
    board_state = [[None] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                board_state[i][j] = Tile(arr[i][j]); board_state[i][j].row, board_state[i][j].col = i, j
    return board_state

b, dict_d = Board(board_state_converter(arr)), {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
b.shift_all_tiles(dict_d[d]);
for i in range(4): print(*[elem.number if elem is not None else 0 for elem in b.board_state[i]])
