# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):

    def merge_sort(a, inversions):
        n=len(a)
        if n==1:
            return a,0
        m=n//2
        x,e= merge_sort(a[:m],0)
        inversions+=e
        y,e= merge_sort(a[m:],0)
        inversions+=e
        d,e= merge(x,y)
        inversions+=e
        return d, inversions

    def merge(b,c):
        f=[]
        inv=0
        bi=0
        ci=0
        while bi!=len(b) and ci!=len(c):
            if b[bi]<=c[ci]:
                f.append(b[bi])
                bi+=1
                inv+=ci
            else:
                f.append(c[ci])
                ci+=1
        inv+=(len(b)-bi)*ci
        f+=b[bi:]
        f+=c[ci:]
        return f,inv

    return merge_sort(a,0)[1]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
