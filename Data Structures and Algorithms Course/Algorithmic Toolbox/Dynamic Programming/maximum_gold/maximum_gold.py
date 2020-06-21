# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    import math
    n=len(weights)
    value=[[None]*(capacity+1) for i in range(n+1)]
    for i in range(n+1): value[i][0]=0
    value[0]=[0 for i in range(capacity+1)]

    # for i in range(1,n+1):
    #     for j in range(1, capacity+1):
    #         value[i][j]=value[i-1][j]
    #         if weights[i-1]<=j:
    #             val=value[i-1][j-weights[i-1]] + weights[i-1]
    #             if value[i][j] < val:
    #                 value[i][j] =val
    # return value[n][capacity]
    def recurse(x,y):
        if x<0 or y<0:
            return -math.inf
        if value[x][y] is not None:
            return value[x][y]
        value[x][y] = max((recurse((x-1),(y-weights[x-1])) + weights[x-1]), (recurse(x-1,y)))
        return value[x][y]
    return recurse(n,capacity)



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
