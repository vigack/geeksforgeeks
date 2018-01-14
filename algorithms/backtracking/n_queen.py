"""
N queen problem
ref: https://practice.geeksforgeeks.org/problems/n-queen-problem/0
"""


def n_queen(n):
    board = [[None for i in range(n)] for j in range(n)]
    solves = []
    backtrack(solves, board, 0)


def backtrack(solves, board, level):
    if level == len(board):
        solves.append([x.index('Q') for x in board])
        return True
    for i in range(len(board)):
        if board[level][i] != 'X':
            pass

