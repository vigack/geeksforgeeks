class Graph:
    """
    Directed graph implements by adjacent list.
    """
    def __init__(self, n):
        self.n = n
        self.lst = [[] for i in range(n)]

    def adj(self, i):
        return self.lst[i]

    def connect(self, i, j):
        self.lst[i].append(j)

    def size(self):
        return self.n

