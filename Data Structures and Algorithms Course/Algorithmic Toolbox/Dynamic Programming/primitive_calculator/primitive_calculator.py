# python3


def compute_operations(n):
    import math
    assert 1 <= n <= 10 ** 6
    min_no=[0]*(n+1)
    min_factors=[[i] for i in range(n+1)]
    temp=[math.inf]*3
    for i in range(n+1):
        if i % 2 == 0:
            temp[0]=min_no[i//2] +1
        if i % 3 == 0:
            temp[1]=min_no[i//3] +1
        if i > 1:
            temp[2]=min_no[i-1] +1
        else:
            continue
        min_no[i]=min(temp)
        if temp[0] == min_no[i]:
            min_factors[i]=min_factors[i//2]+[i]
        elif temp[1] == min_no[i]:
            min_factors[i]=min_factors[i//3]+[i]
        else:
            min_factors[i]=min_factors[i-1]+[i]
        temp=[math.inf]*3
    return min_factors[n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
