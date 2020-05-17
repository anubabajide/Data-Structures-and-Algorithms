#Uses python3

import sys
from collections import deque


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    prev = [None] * len(adj)
    seen = [False] * len(adj)
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        for v in adj[cur]:
            if reachable[v] == 0:
                queue.append(v)
                reachable[v] = 1
    reachable[s] = 1
    for _ in range(len(adj)-1):
        for index in range(len(adj)):
            for i in range(len(adj[index])):
                if distance[adj[index][i]] > distance[index] + cost[index][i]:
                    distance[adj[index][i]] = distance[index] + cost[index][i]
                    prev[adj[index][i]] = index

    for index in range(len(adj)):
        for i in range(len(adj[index])):
            if distance[adj[index][i]] > distance[index] + cost[index][i]:
                node = index
                while not seen[node] :
                    seen[node] = True
                    queue.append(node)
                    node = prev[node]
    
                while queue:
                    cur = queue.popleft()
                    for v in adj[cur]:
                        if (shortest[v] == 1) and (reachable[v]==1):
                            queue.append(v)
                            shortest[v] = 0
    
    return


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

