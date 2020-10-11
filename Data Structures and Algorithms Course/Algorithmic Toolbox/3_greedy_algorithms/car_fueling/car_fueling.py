# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    i=0
    count=0
    capacity=m
    stations=len(stops)
    while True:
        if m >= d:
            return count
        start=i
        while i<=stations-1:
            if stops[i]<=m:
                i+=1
            else:
                break
        count+=1
        m=stops[i-1]+capacity
        if start==i:
            return -1



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
