def queens(board, row, size):
    if row == size:
        print(board)
    for i in range(size):
        allowed = True
        for j in range(row):
            if board[j] in [i, i + row - j, i - row + j]:
                allowed = False
        if allowed:
            board[row] = i
            queens(board, row + 1, size)

size = 12
board = [-1 for i in range(size)]

queens(board, 0, size)
