# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    def my_majority_element(l,r):
        if l==r:
            return elements[l]
        m=(l+r)//2
        t=(r-l+1)/2
        left= my_majority_element(l,m)
        right=my_majority_element(m+1,r)
        if left==right:
            return left
        countl=0
        countr=0
        for x in range(l,r+1):
            if elements[x]==left:
                countl+=1
            elif elements[x]==right:
                countr+=1
            if countl>t:
                return left
            if countr>t:
                return right
        return False
    l=0
    r=len(elements)-1
    if my_majority_element(l,r)==False:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
