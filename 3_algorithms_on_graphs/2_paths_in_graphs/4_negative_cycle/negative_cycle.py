#python3

import sys


def negative_cycle(adj, cost):
    inf = float('inf')
    dist = [1001] * len(adj)
    dist[0] = 0
    for _ in range(len(adj)-1):
        for index in range(len(adj)):
            for i in range(len(adj[index])):
                if dist[adj[index][i]] > dist[index] + cost[index][i]:
                    dist[adj[index][i]] = dist[index] + cost[index][i]

    for index in range(len(adj)):
        for i in range(len(adj[index])):
            if dist[adj[index][i]] > dist[index] + cost[index][i]:
                return 1
    return 0


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
    print(negative_cycle(adj, cost))
