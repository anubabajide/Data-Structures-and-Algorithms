# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    import math
    if keys[0]>query  or query>keys[-1]:
        return -1
    r=len(keys)-1
    l=0
    mid=0
    count=0
    while keys[mid] != query:
        if keys[l]>query or query>keys[r]:
            return -1
        mid=(l+r)//2
        if keys[mid]>query:
            r=mid-1
        if keys[mid]<query:
            l=mid+1
    return mid


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
