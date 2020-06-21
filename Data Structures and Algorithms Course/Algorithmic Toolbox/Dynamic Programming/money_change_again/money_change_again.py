# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    min_no=[0]*(money+1)
    for i in range(money+1):
        if i>=4:
            min_no[i]=min(min_no[i-1]+1, min_no[i-3]+1, min_no[i-4]+1)
        elif i>=3:
            min_no[i]=min(min_no[i-1]+1, min_no[i-3]+1)
        elif i>=1:
            min_no[i]=min_no[i-1]+1
        else:
            min_no[i]=0
    return min_no[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
