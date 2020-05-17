#python3

import sys
import queue

class BiDij:
    def __init__(self, n):
        self.n = n                              # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [[False]*n, [False]*n]   # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search

    def clear(self):
        #"""Reinitialize the data structures for the next query after the previous query."""
        self.d = [[self.inf]*self.n, [self.inf]*self.n]
        for v in self.workset:
            self.visited[0][v] = self.visited[1][v] =False

        del self.workset[0:len(self.workset)]

    def visit(self, q, side, index, cost, adj):
        #"""Try to relax the distance to node v from direction side by value dist."""
        self.visited[side][index] = True
        self.workset.append(index)
        for v in range(len(adj[side][index])):
            if self.d[side][adj[side][index][v]] > self.d[side][index] + cost[side][index][v]: 
                self.d[side][adj[side][index][v]] = self.d[side][index] + cost[side][index][v]
                q[side].put((self.d[side][adj[side][index][v]], adj[side][index][v]))

    def get_path(self):
        dist = self.inf
        for i in self.workset:
            dist = min(self.d[0][i] + self.d[1][i], dist)
        return dist

    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.d[0][s] = 0
        self.d[1][t] = 0
        q[0].put((self.d[0][s], s))
        q[1].put((self.d[1][t], t))
        while not (q[0].empty() and q[1].empty()):
            try:
                _, index = q[0].get_nowait()
                while self.visited[0][index]:
                    _, index = q[0].get_nowait()
                self.visit(q, 0, index, cost, adj)
                if self.visited[1][index]:
                    return self.get_path()
            except queue.Empty:
                pass

            try:
                _, index = q[1].get_nowait()
                while self.visited[1][index]:
                    _, index = q[1].get_nowait()
                self.visit(q, 1, index, cost, adj)
                if self.visited[0][index]:
                    return self.get_path()
            except queue.Empty: 
                pass
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)

    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
