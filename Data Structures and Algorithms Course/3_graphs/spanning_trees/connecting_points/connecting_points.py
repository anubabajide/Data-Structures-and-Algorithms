#python3
import sys
import math
from collections import deque

def distance(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

def distance2(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def minimum_distance(x, y):
    number = len(x)
    result = 0
    cost = [float('inf')] * number
    prev = [None] * number
    u = 0
    cost[u] = 0
    prior_Q = [(cost[i], i) for i in range(number)]
    seen = [False] * number
    for _o in range(number):
        _, v = min(prior_Q)
        prior_Q[v] = (float('inf'), v)
        seen[v] = True
        for z in range(number):
            if (z != v) and (not seen[z]):  
                temp = distance((x[z], y[z]), (x[v], y[v]))
                if cost[z] > temp:
                    cost[z] = temp
                    prev[z] = v
                    prior_Q[z] = (cost[z], z)
    for i in range(number):
        if prev[i] is not None:
            temp = distance2((x[i], y[i]), (x[prev[i]], y[prev[i]])) 
            result += temp

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
