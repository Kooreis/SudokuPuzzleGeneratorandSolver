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