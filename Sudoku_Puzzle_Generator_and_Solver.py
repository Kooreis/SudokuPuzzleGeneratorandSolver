```python
import random

def generate_board():
    base  = 3
    side  = base*base
    nums  = sample(range(1, side + 1), side)
    board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
    rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ] 
    cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]            
    board = [[board[r][c] for c in cols] for r in rows]
    squares = side*side
    empties = squares * 3//4
    for p in map(lambda _: (randrange(side), randrange(side)), range(empties)):
        board[p[0]][p[1]] = 0
    return board

def print_board(board):
    num_len = len(str(max(map(max, board))))
    for line in board:
        print("[" + "][".join(f"{n or '.':{num_len}}" for n in line) + "]")

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def main():
    board = generate_board()
    print_board(board)
    solve(board)
    print("___________________")
    print_board(board)

if __name__ == "__main__":
    main()
```