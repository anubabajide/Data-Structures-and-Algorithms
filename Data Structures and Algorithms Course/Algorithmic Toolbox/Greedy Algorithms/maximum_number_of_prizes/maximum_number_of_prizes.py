# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    sum=1
    i=1
    while sum<=n:
        summands.append(i)
        i+=1
        sum+=i
    summands[-1]+=(n-sum+i)


    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
