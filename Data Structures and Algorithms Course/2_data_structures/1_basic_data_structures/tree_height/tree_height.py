# python3

import sys
import threading

class Node:
    def __init__(self, val):
        self.val=val
        self.children=[]
        self.level=None

    def add_child(self, node):
        self.children.append(node)


def compute_height(n, parents):
    # Replace this code with a faster implementation
    tree=[Node(i) for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root=i
            tree[i].level = 1
        else:
            tree[parents[i]].add_child(tree[i])

    stack=[tree[root]]
    max_height=0
    while stack:
        cur=stack.pop()
        for i in cur.children:
            i.level=cur.level+1
        stack.extend(cur.children)
        max_height=max(cur.level, max_height)

    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
