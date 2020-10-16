#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj):
    order = []
    visited = [False] * len(adj)


    def explore(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w)
        order.append(v)


    for i in range(len(adj)):
        if not visited[i]:
            explore(i)

    return reversed(order)

def number_of_strongly_connected_components(adj):
    result = 0
    adj_inv = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            adj_inv[j].append(i)
        
    order = dfs(adj_inv)
    visited = [False] * len(adj)


    def explore(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w)


    for i in order:
        if not visited[i]:
            explore(i)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
