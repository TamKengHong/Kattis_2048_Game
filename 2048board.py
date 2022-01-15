arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))
d = int(input())

class Board:
    def __init__(self, board_state):
        self.board_state = board_state

    def move(self, start_pos, end_pos):
        piece = self.board_state[start_pos[0]][start_pos[1]]
        piece.row, piece.col = end_pos[0], end_pos[1]
        self.board_state[end_pos[0]][end_pos[1]] = piece
        self.board_state[start_pos[0]][start_pos[1]] = None

    def shift_all_tiles(self, direction): # works
        if direction == (0, -1): #left
            for i in range(4):
                for j in range(4):
                    tile = self.board_state[i][j]
                    if tile is not None:
                        tile.shift((0,-1), self)
        elif direction == (-1, 0): #up
            for i in range(4):
                for j in range(4):
                    tile = self.board_state[j][i] #shift column by column upwards
                    if tile is not None:
                        tile.shift((-1, 0), self)
        elif direction == (0, 1): #right
            for i in range(4):
                for j in range(4):
                    tile = self.board_state[i][3 - j] #shift tiles in reverse order as leftwards
                    if tile is not None:
                        tile.shift((0, 1), self)
        elif direction == (1, 0): #down
            for i in range(4):
                for j in range(4):
                    tile = self.board_state[3 - j][i] #shift tiles in reverse order as upwards
                    if tile is not None:
                        tile.shift((1, 0), self)


class Tile:
    def __init__(self, number):
        self.number = number
        self.row = None
        self.col = None
        self.merged = False

    def shift(self, direction, board):
        while self.row + direction[0] in range(4) and self.col + direction[1] in range(4):
            new_pos = (self.row + direction[0], self.col + direction[1])
            tile = board.board_state[new_pos[0]][new_pos[1]]
            if tile is None:
                board.move((self.row, self.col), new_pos)
            elif tile.number == self.number and tile.merged == False:
                self.number *= 2
                board.move((self.row, self.col), new_pos)
                self.merged = True
                break
            else:
                break



def board_state_converter(arr): #works
    board_state = [[None] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                board_state[i][j] = Tile(arr[i][j])
                board_state[i][j].row, board_state[i][j].col = i, j
    return board_state

def print_board_state(board_state): #works
    for i in range(4):
        arr = []
        for elem in board_state[i]:
            if elem is not None:
                arr.append(elem.number)
            else:
                arr.append(0)
        print(*arr)

b = Board(board_state_converter(arr))

if d == 0:
    b.shift_all_tiles((0, -1)) #left
elif d == 1:
    b.shift_all_tiles((-1, 0)) #up
elif d == 2:
    b.shift_all_tiles((0, 1)) #right
elif d == 3:
    b.shift_all_tiles((1, 0)) # down

print_board_state(b.board_state)


