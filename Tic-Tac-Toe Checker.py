def is_solved(board):
    for i in board:
        if set(i)=={1}:
            return 1
        elif set(i)=={2}:
            return 2
    for i in range(3):
        if  set([board[0][i], board[1][i], board[2][i]])=={1}:
            return 1
        elif set([board[0][i], board[1][i], board[2][i]])=={2}:
            return 2
    if  set([board[0][0], board[1][1], board[2][2]])=={1}:
            return 1
    elif set([board[0][0], board[1][1], board[2][2]])=={2}:
            return 2
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                return -1
    return 0
         

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
is_solved(board)
rand_colors=['green', 'lime', 'dark green', 'blue', 'cyan', 'dark blue', 'red', 'orange', 'yellow', 'purple', 'violet','pink','grey']