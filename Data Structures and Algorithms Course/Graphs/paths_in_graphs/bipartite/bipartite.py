#python3

import sys
from collections import deque

def bipartite(adj):
    color = [None] * len(adj)
    queue = deque([0])
    color[0] = True
    parent = None
    while queue:
        cur = queue.popleft()
        for v in adj[cur]:
            if color[v] is None:
                queue.append(v)
                color[v] = not color[cur]
            else:
                if color[v] is color[cur]:
                    return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
