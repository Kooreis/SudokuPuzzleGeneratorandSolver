def print_board(board):
    num_len = len(str(max(map(max, board))))
    for line in board:
        print("[" + "][".join(f"{n or '.':{num_len}}" for n in line) + "]")