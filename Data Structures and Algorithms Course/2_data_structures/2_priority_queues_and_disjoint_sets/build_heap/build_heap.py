# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)

    def sift_down(i):
        min_index = i
        i = 'v'
        while i != min_index:
            i = min_index
            left = (2*i)+1
            right = (2*i)+2
            if left < n and data[left] < data[min_index]:
                min_index = left
            if right < n and data[right] < data[min_index]:
                min_index = right
            if min_index != i:
                swaps.append((i, min_index))
                data[min_index], data[i] = data[i], data[min_index]
            else:
                return

    for i in range(n//2, -1, -1):
        sift_down(i)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
