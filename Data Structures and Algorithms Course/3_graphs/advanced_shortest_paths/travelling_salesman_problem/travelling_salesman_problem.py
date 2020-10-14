#python3


import sys
from heapq import heappush, heappop, heapify


# Maximum allowed edge length
maxlen = 2 * 10**6


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
        self.level = [0] * n
        self.rank = [0] * n
        self.shortcut_cover = [0] * n
        k = 5
        count = 1

##################################################################################### Pre-processing Code #####################################################################################
        
        for i in range(n): 
            heappush(self.q,(self.compute_importance(i, False), i))
        while self.q:
            _, index = heappop(self.q)                           
            temp = self.compute_importance(index)  
            run = 0
            while self.q and (temp > self.q[0][0]) and (run < 100):                          
                run += 1
                heappush(self.q, (temp, index))
                _, index = heappop(self.q)
                temp = self.compute_importance(index)
            
            self.rank[index] = count
            count += 1
            self.visited[index] = True               
            if self.adj[0][index]:
                for v in range(len(self.adj[1][index])):                             
                    check = max(self.cost[1][index]) + max(self.cost[0][index])     
                    to_add = []                                                     
                    self.witness(self.adj[1][index][v], self.cost[1][index][v], to_add, check, k, index)    
                    self.shortcut(v, to_add)                                        

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
    
    def witness(self, s, a_part, to_add, check, k, v):               
        dist = self.bidistance[0]                
        seen = set()                  
        dist[s] = 0                                     
        self.workset.add(s)
        priority_queue = [(dist[s], s)]                 
        count = 0                                       
        while (priority_queue) and (count < 6):
            count += 1             
            _, index = heappop(priority_queue)          
            while priority_queue and (index in seen):         
                _, index = heappop(priority_queue)
            if not priority_queue and (index in seen):
                break
            seen.add(index)                     
            for i in range(len(self.adj[0][index])):    
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


    def add_arc(self, u, v, c):                     
        def update(adj, cost, u, v, c):             
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

    def shortcut(self, v, to_add):               
        for x, y, cost in to_add:                 
            self.add_arc(x, y, cost)                     
            
    def compute_importance(self, v, calc_neighbors = True):
        neighbors = 0                                       
        if calc_neighbors:
            for i in self.adj[0][v] + self.adj[1][v]:
                self.level[i] = max(self.level[v] + 1, self.level[i])
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

INF = float('inf') 


# Returns the adjacency matrix of a graph on the given vertices with edges equal to the distances between
# those nodes in the initial road network
def make_graph(ch, vertices):
    n = next(vertices)
    vertices = list(vertices)
    assert n == len(vertices)
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            l = ch.query(vertices[i]-1, vertices[j]-1)
            graph[i][j] = l if l != -1 else INF
    return graph


# Returns the length of the shortest circular path visiting all the nodes at least once
def optimal_path(graph):
    # Implement this function yourself
    global all_seen, n

    # Recursive function
    def cost(S, i):
        # If all points have been visited, add the cost of last visited point to origin
        if S == all_seen:
            return graph[i][0]
        
        # Check if the DP array has encountered this configuration before
        if dp[i][S] != INF:
            return dp[i][S]
        
        # Update value of DP array to store current configuration then return value
        # This list comprehension checks for all nodes that have not been visited excluding origin point using bit manipulation
        dp[i][S] = min([cost(S|(1<<j), j) + graph[i][j] for j in range(n) if (j != 0) and (S&(1<<j) == 0)])
        return dp[i][S]

    n = len(graph)
    # Create bit mask for when all the nodes are visited
    all_seen = (1 << n) - 1
    
    # Create DP Array for all configurations
    #  E.G For points 1, 2, 3
    #  bit mask for visited all is --- 111 (8(2^3))
    #  And DP Array is 
    #  |_____|1  | 2 | 3 |
    #  | 000 |___|___|___|
    #  | 001 |___|___|___|
    #  | 010 |___|___|___|
    #  | 011 |___|___|___|
    #  | 100 |___|___|___|
    #  | 101 |___|___|___|
    #  | 110 |___|___|___|
    #  | 111 |___|___|___|
    #  
    # Complexity is O((2^n)*n)

    dp = [[INF]*all_seen for _ in range(n)]
    x = cost(1, 0)
    
    return -1 if x == INF else x


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
        print(optimal_path(make_graph(ch, readl())))
