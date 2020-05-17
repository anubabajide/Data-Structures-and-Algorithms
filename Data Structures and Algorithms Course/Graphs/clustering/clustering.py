#Uses python3
import sys
import math

class Disjoint_Set:
    def __init__(self, points):
        n_tables = points
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[dst_parent] >= self.ranks[src_parent]:
            self.parents[src_parent] = dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
        else:
            self.parents[dst_parent] = src_parent
            
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        if self.parents[table] == table:
            return table
        self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def distance2(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def clustering(x, y, k):
    number = len(x)
    edges = [(distance2((x[i], y[i]), (x[j], y[j])), i, j) for i in range(number-1) for j in range(i+1, number)]
    edges.sort(key = lambda x: x[0])
    clusters = Disjoint_Set(number)
    count = 0

    for result, i, j in edges:
        result
        if count >= (number - k):
            if clusters.get_parent(i) != clusters.get_parent(j):
                break            
        elif clusters.merge(i, j):
            count += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
