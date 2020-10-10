#python3


import sys
from heapq import heappush, heappop, heapify


# Maximum allowed edge length
# maxlen = 2 * 10**6


class DistPreprocessLarge:
    def __init__(self, n, adj, cost):
        self.n = n
        self.INFINITY = float('inf')
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [None]*n
        self.workset = set()
        self.q = []
        # Levels of nodes for node ordering heuristics
        self.level = [0] * n
        # Positions of nodes in the node ordering
        self.rank = [0] * n
        #Shortcut cover
        self.shortcut_cover = [0] * n
        # Max number of hops
        k = 5
        count = 1

##################################################################################### Pre-processing Code #####################################################################################
        for i in range(n):      # Computing Heuristics for each node to get order 
            heappush(self.q,(self.compute_importance(i, False), i))
        while self.q:
            _, index = heappop(self.q)                          # Get next node to be processed, On each retrieval, recompute importance 
            temp = self.compute_importance(index)  # and check if next node in queue has lower importance
            run = 0
            while self.q and (temp > self.q[0][0]) and (run < 100):                          # Push back to queue if yes
                run += 1
                heappush(self.q, (temp, index))
                _, index = heappop(self.q)
                temp = self.compute_importance(index)
            
            self.rank[index] = count
            count += 1
            self.visited[index] = True               
            if self.adj[0][index]:
                for v in range(len(self.adj[1][index])):                            # For all (incomin  g, Outgoing) edge pair, Check if there exists a witness edge 
                    check = max(self.cost[1][index]) + max(self.cost[0][index])     # Set a check value that is the current path cost being checked
                    to_add = []                                                     # Array to store edges to add
                    self.witness(self.adj[1][index][v], self.cost[1][index][v], to_add, check, k, index)    # Check for witness edges, If no witness edge exists, mark points to add shortcuts 
                    self.shortcut(v, to_add)                                        # Add Relevant Shortcuts

            for i in self.adj[0][index]:  
                ti = len(self.adj[1][i])
                j = 0
                while j < ti:
                    if self.adj[1][i][j] == index:
                        self.adj[1][i][j], self.adj[1][i][ti-1] = self.adj[1][i][ti-1], self.adj[1][i][j]
                        self.cost[1][i][j], self.cost[1][i][ti-1] = self.cost[1][i][ti-1], self.cost[1][i][j]
                        self.adj[1][i].pop()
                        self.cost[1][i].pop()
                        ti -= 1
                        break
                    else:
                        j += 1

            for i in self.adj[1][index]:
                ti = len(self.adj[0][i])
                j = 0
                while j < ti:
                    if self.adj[0][i][j] == index:
                        self.adj[0][i][j], self.adj[0][i][ti-1] = self.adj[0][i][ti-1], self.adj[0][i][j]
                        self.cost[0][i][j], self.cost[0][i][ti-1] = self.cost[0][i][ti-1], self.cost[0][i][j]
                        self.adj[0][i].pop()
                        self.cost[0][i].pop()
                        ti -= 1
                        break
                    else:
                        j += 1

        self.visited = [None]*n

##################################################################################### Pre-processing Functions #####################################################################################
    def witness(self, s, a_part, to_add, check, k, v):               # Perform regular Dijkstra with some modifications
        dist = self.bidistance[0]               # Distance to each node from source 
        seen = set()                  # If node has been processed before
        dist[s] = 0                                     # Source node distance = 0
        self.workset.add(s)
        priority_queue = [(dist[s], s)]                 # Priority queue initialized with source node
        count = 0                                       # Stop Dijkstra optimization to specify threshold
        while (priority_queue) and (count < 6):
            count += 1             
            _, index = heappop(priority_queue)          # Pick topmost Item and check if it has been processed already
            while priority_queue and (index in seen):         
                _, index = heappop(priority_queue)
            if not priority_queue and (index in seen):
                break
            seen.add(index)                     # Mark item as seen
            for i in range(len(self.adj[0][index])):    # Check neighbors if node can be relaxed, while also checking if path length is already over the current path being witnessed. Avoid node being relaxed v
                if (self.adj[0][index][i] != v) and (dist[self.adj[0][index][i]] > dist[index] + self.cost[0][index][i]) and (dist[index] + self.cost[0][index][i] < check):
                    self.workset.add(self.adj[0][index][i])
                    dist[self.adj[0][index][i]] = dist[index] + self.cost[0][index][i]
                    heappush(priority_queue, (dist[self.adj[0][index][i]], self.adj[0][index][i]))
        
        for t in range(len(self.adj[0][v])): 
            if dist[self.adj[0][v][t]] > a_part + self.cost[0][v][t]:
                to_add.append((s, self.adj[0][v][t], a_part + self.cost[0][v][t]))
        
        for i in self.workset:
            dist[i] = self.INFINITY
        self.workset.clear


    def add_arc(self, u, v, c):                     # Add a shortcut from node u to v
        def update(adj, cost, u, v, c):             # Check if there is an edge already from u to v
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)
        self.shortcut_cover[u] += 1
        self.shortcut_cover[v] += 1
        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    def shortcut(self, v, to_add):               # Makes shortcuts for contracting node v
        for x, y, cost in to_add:                # Create Shortcuts for all nodes, keep count of all added shortcuts, 
            self.add_arc(x, y, cost)                     # and then add keep count of all nodes that have shortcuts to or from them
            
    def compute_importance(self, v, calc_neighbors = True):
        neighbors = 0                                       # Compute Importance for given node
        if calc_neighbors:
            for i in self.adj[0][v] + self.adj[1][v]:
                self.level[i] = max(self.level[v] + 1, self.level[i]) # Update level of every neighbour
                if self.visited[i]: 
                    neighbors += 1
        
        return ((len(self.adj[0][v]) * len(self.adj[1][v])) - len(self.adj[0][v]) - len(self.adj[1][v]) + neighbors + self.shortcut_cover[v] + self.level[v])

############################################################################################ Query Code ############################################################################################
    def mark_visited(self, v, side):
        if self.visited[v] is None:
            self.visited[v] = side
        elif self.visited[v] == (1 - side):
            self.visited[v] = 2
    
    def clear(self):
        for v in self.workset:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[v] = None
        self.workset.clear()

    def visit(self, q, side, index):
        self.mark_visited(index, side)
        for v in range(len(self.adj[side][index])):
            self.workset.add(self.adj[side][index][v])
            if self.bidistance[side][self.adj[side][index][v]] > self.bidistance[side][index] + self.cost[side][index][v]: 
                self.bidistance[side][self.adj[side][index][v]] = self.bidistance[side][index] + self.cost[side][index][v]
                heappush(q[side], (self.bidistance[side][self.adj[side][index][v]], self.adj[side][index][v]))

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        estimate = self.INFINITY
        q = [[], []]
        self.bidistance[0][s] = 0
        self.bidistance[1][t] = 0
        self.workset.add(s)
        self.workset.add(t)
        heappush(q[0], (self.bidistance[0][s], s))  
        heappush(q[1], (self.bidistance[1][t], t))  
        while q[0] or q[1]:
            if q[0]:
                _, index = heappop(q[0])
                while q[0] and ((self.visited[index] == 0) or (self.visited[index] == 2)):
                    _, index = heappop(q[0])
                if self.bidistance[0][index] <= estimate:
                    self.visit(q, 0, index)
                if estimate > self.bidistance[0][index] + self.bidistance[1][index]:
                    estimate = self.bidistance[0][index] + self.bidistance[1][index] 
            
            if q[1]:
                _, index2 = heappop(q[1])
                while q[1] and ((self.visited[index2] == 1) or (self.visited[index2] == 2)):
                    _, index2 = heappop(q[1])
                if self.bidistance[1][index2] <= estimate:
                    self.visit(q, 1, index2)
                if estimate > self.bidistance[0][index2] + self.bidistance[1][index2]:
                    estimate = self.bidistance[0][index2] + self.bidistance[1][index2]
        del index, index2
        
        return -1 if estimate == self.INFINITY else estimate


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

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))