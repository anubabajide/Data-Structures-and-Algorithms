#python3

import sys


def acyclic(adj):
    visited = [False] * len(adj)
    ans = True

    def explore(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                if explore(w) == 1:
                    return 1
            else:
                return 1
        visited[v] = False
        return 0


    for i in range(len(adj)):
        if not visited[i]:
            ans = explore(i)

        if ans == 1:
            return ans
    return ans 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
