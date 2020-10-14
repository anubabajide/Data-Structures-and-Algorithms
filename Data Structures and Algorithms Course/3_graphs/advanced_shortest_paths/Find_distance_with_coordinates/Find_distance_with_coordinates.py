#python3

import sys
import queue
import math

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.d = [self.inf]*n
        self.visited = [False]*n
        self.workset = []
        # Coordinates of the nodes
        self.x = x
        self.y = y
        #Source, Destination and Potential Function
        self.s = None
        self.t = None
        self.constant = 0

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self, s, t):
        self.d = [self.inf]*self.n
        for v in self.workset:
            self.visited[v] = False
        del self.workset[0:len(self.workset)]
        self.s = (self.x[s], self.y[s])
        self.t = (self.x[t], self.y[t])
        self.constant = math.sqrt((self.s[0]-self.t[0])**2 + (self.s[1]-self.t[1])**2)

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, index):
        # Implement this method yourself
        self.visited[index] = True
        self.workset.append(index)
        for v in range(len(self.adj[index])):
            if self.d[self.adj[index][v]] > self.d[index] + self.cost[index][v]: 
                self.d[self.adj[index][v]] = self.d[index] + self.cost[index][v]
                q.put((self.potential(self.adj[index][v]), self.adj[index][v]))

    def potential(self, v):
        return (self.d[v] - self.constant + math.sqrt((self.x[v]-self.t[0])**2 + (self.y[v]-self.t[1])**2))

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear(s, t)
        q = queue.PriorityQueue()
        self.d[s] = 0
        q.put((self.potential(s), s))
        while not q.empty():
            try:
                _, index = q.get_nowait()
                while self.visited[index]:
                    _, index = q.get_nowait()
            except:
                break
            self.visit(q, index)
            if self.visited[t]:
                return self.d[t]
        # Implement the rest of the algorithm yourself
        return self.d[t] if self.d[t]<self.inf else -1

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    why, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(why):
        s, t = readl()
        print(astar.query(s-1, t-1))
