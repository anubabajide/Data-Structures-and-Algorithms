#ython3

import sys
from collections import deque
from heapq import heappush, heapify, heappop

def distance(adj, cost, s, t):
    inf = float('inf')
    dist = [inf] * len(adj)
    prev = [None] * len(adj)
    bit_array = [False] * len(adj)
    dist[s] = 0
    priority_queue = [(dist[i], i) for i in range(len(adj))]
    heapify(priority_queue)
    count = 0
    while count < len(adj):
        _, index = heappop(priority_queue)
        while bit_array[index]:
            _, index = heappop(priority_queue)
        bit_array[index] = True
        count += 1
        for i in range(len(adj[index])):
            if dist[adj[index][i]] > dist[index] + cost[index][i]:
                dist[adj[index][i]] = dist[index] + cost[index][i]
                prev[adj[index][i]] = index
                heappush(priority_queue, (dist[adj[index][i]], adj[index][i]))
        if bit_array[t]:
            return dist[t] if dist[t] < inf else -1
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
