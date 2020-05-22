# python3
from  _collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    window=deque()
    #An element is irrelevant if
    #1. there is a larger value that comes after it
    #2. it is outside the window range
    for i in range(m):
        #process relevant elements into queue of size k
        while window and sequence[i] >= sequence[window[-1]]:
            window.pop()
        window.append(i)

    for i in range(m, len(sequence)):
        #return max value, remove irrelevant elements and add new element
        maximums.append(sequence[window[0]])
        while window and  window[0] <= i-m:
            window.popleft()
        while window and sequence[i] >= sequence[window[-1]]:
            window.pop()
        window.append(i)

    maximums.append(sequence[window[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

