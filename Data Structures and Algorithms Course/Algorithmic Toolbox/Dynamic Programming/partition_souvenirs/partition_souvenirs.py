# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    import math

    def recurse(x,y):
        if x<0 or y<0:
            return -math.inf
        if custom_array[x][y] is not None:
            return custom_array[x][y]
        custom_array[x][y] = max((recurse((x-1),(y-values[x-1])) + values[x-1]), (recurse(x-1,y)))
        return custom_array[x][y]

    def backtrack(x,y):
        if x<=0 or y<=0:
            return
        if custom_array[x][y]==custom_array[x-1][y-values[x-1]]:
            check[x-1]=1
            backtrack(x-1,y-values[x-1])
        else:
            backtrack(x-1,y)
        return

    #First iteration
    n=len(values)
    m=sum(values)
    if n<3 or m%3 !=0:
        return 0
    w=m//3
    custom_array=[[None]*(w+1) for i in range(n+1)]
    for i in range(n+1): custom_array[i][0]=0
    custom_array[0]=[0 for i in range(w+1)]
    check=[0]*n
    recurse(n,w)
    # print(custom_array)
    if custom_array[n][w]!=w:
        return 0
    backtrack(n,w)
    # print(check)
    temp=[values[i] for i in range(n) if check[i]==0]
    values=temp

    #Second Iteration
    n=len(values)
    if n<2:
        return 0
    custom_array=[[None]*(w+1) for i in range(n+1)]
    for i in range(n+1): custom_array[i][0]=0
    custom_array[0]=[0 for i in range(w+1)]
    check=[0]*n
    recurse(n,w)
    if custom_array[n][w]!=w:
        return 0
    return 1


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
