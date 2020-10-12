# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    def add_start(x):
        return (x,'0')

    def add_stop(x):
        return (x,'2')

    def add_point(x):
        return (x[1],'1',x[0])

    starts=list(map(add_start, starts))
    stops=list(map(add_stop, ends))
    points=list(map(add_point, list(enumerate(points))))
    total=starts+stops+points
    total=sorted(total, key= lambda x: (x[0]*10)+int(x[1]))
    count=0
    res=[0]*len(points)
    for i in total:
        if i[1]=='0':
            count+=1
        elif i[1]=='2':
            count-=1
        elif i[1]=='1':
            res[i[2]]=count
    return res


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
