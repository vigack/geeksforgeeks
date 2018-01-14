"""A rat in a maze backtracking solution"""


solves = []


def find_path(maze, n):
    traveled = [[False for i in range(n)] for j in range(n)]
    traveled[0][0] = True
    if backtrack(maze, [], (0, 0), traveled):
        print(solves)
    else:
        print("No escape path!")


def next_move(maze, current, traveled):
    moves = []
    x, y = current
    for dx, dy, direction in [[1, 0, 'D'], [-1, 0, 'U'], [0, 1, 'R'], [0, -1, 'L']]:
        if -1 < x + dx < len(maze) and -1 < y + dy < len(maze):
            if not traveled[x+dx][y+dy] and maze[x+dx][y+dy]==1:
                moves.append(((x+dx, y+dy), direction))
    return moves


def backtrack(maze, path, current, traveled):
    if current[0] == len(maze)-1 and current[1] == len(maze) - 1:
        return True
    for nxt, direction in next_move(maze, current, traveled):
        path.append(direction)
        traveled[nxt[0]][nxt[1]] = True
        if backtrack(maze, path, nxt, traveled):
            solves.append(''.join(path))
        else:
            path.pop()
    return False
