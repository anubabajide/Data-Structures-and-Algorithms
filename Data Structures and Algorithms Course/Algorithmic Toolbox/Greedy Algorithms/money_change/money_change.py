# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    sol=0
    rem=money%10
    sol+=money//10
    if rem==0:
        return int(sol)
    else:
        sol+=rem//5
        rem=rem%5
        if rem==0:
            return int(sol)
        else:
            return(sol+rem)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
