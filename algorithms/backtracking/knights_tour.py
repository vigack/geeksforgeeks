"""
The knight's tour solution
"""


def tour():
    """fuck the chess board!"""
    board = [[None for i in range(8)] for j in range(8)]
    board[0][0] = 0
    if backtrack(board, (0, 0), 1):
        print(board)
    else:
        print("No valid solve!")


def next_move(curr, board):
    """return next moves as( a turple list"""
    moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    nxts = [(curr[0]+x, curr[1]+y) for x, y in moves]
    nxts = list(filter(lambda p: -1 < p[0] < 8 and -1 < p[1] < 8, nxts))
    nxts = list(filter(lambda p: board[p[0]][p[1]] is None, nxts))
    return nxts


def heuristic(curr, board):
    """optimistic"""
    moves = []
    for nxt in next_move(curr, board):
        board[nxt[0]][nxt[1]] = -1
        moves.append((nxt, len(next_move(nxt, board))))
        board[nxt[0]][nxt[1]] = None
        moves.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], moves))


def backtrack(board, current, count):
    """backtracking"""
    if count == 63:
        return True
    for nxt in next_move(current, board):
        board[nxt[0]][nxt[1]] = count
        if backtrack(board, nxt, count+1):
            return True
        else:
            board[nxt[0]][nxt[1]] = None
    return False


tour()
