# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x:x[1])
    j=0
    res=[]
    a=len(segments)
    while j<a:
        i=segments[j][1]
        while segments[j][0] <= i <= segments[j][1]:
            j+=1
            if j==a:
                break
        res.append(i)
    return res


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
