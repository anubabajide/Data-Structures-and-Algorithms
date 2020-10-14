# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):

    def distance(x,y):
        return (x[0]-y[0])**2+(x[1]-y[1])**2

    def closest_points(A):
        n=len(A)
        if n==2:
            if A[0][1]>A[1][1]:
                A=A[::-1]
            return A, distance(A[0],A[1])

        if n==1:
            return A, float("inf")

        mid = n//2
        B,left=closest_points(A[:mid])
        if left==0: return A, left
        C,right=closest_points(A[mid:])
        if right==0: return A, right
        d=min(left,right)
        A=merge(B,C)
        res=select_point(A, d, mid)
        return A,res

    def merge(b,c):
        f=[]
        bi=0
        ci=0
        while bi!=len(b) and ci!=len(c):
            if b[bi][1]<=c[ci][1]:
                f.append(b[bi])
                bi+=1
            else:
                f.append(c[ci])
                ci+=1
        f+=b[bi:]
        f+=c[ci:]
        return f

    def select_point(A, d, mid):
        real=(A[mid][0]+A[mid-1][0])/2
        newlist=[]
        n=0
        for i in A[mid-1::-1]:
            if i[0] < real-d:
                break
            newlist.append(i)
            n+=1
        for i in A[mid:]:
            if i[0] > real+d:
                break
            newlist.append(i)
            n+=1
        for i in range(n):
            for j in range(i+1,n):
                if j-i>6:
                    break
                d_prime = distance(newlist[i], newlist[j])
                if d_prime==0: return d_prime
                d=min(d,d_prime)
        return d

    if type(points)!= list:
        return 0.0000
    if len(points)==2:
        return distance(points[0],points[1])

    points=sorted(points, key= lambda x:x[0])
    return closest_points(points)[1]


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
