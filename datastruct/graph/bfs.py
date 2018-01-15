from .graph import *


def bfs(graph, vert):
    visited = [False]*graph.size()
    queue = [vert]
    visited[vert] = True
    res = []
    while queue:
        curr = queue.pop(0)
        res.append(curr)
        for i in graph.adj(curr):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return res


def main():
    g = Graph(4)
    g.connect(0, 1)
    g.connect(0, 2)
    g.connect(1, 2)
    g.connect(2, 0)
    g.connect(2, 3)
    g.connect(3, 3)
    print(' '.join(list(map(str, bfs(g, 2)))))


main()
