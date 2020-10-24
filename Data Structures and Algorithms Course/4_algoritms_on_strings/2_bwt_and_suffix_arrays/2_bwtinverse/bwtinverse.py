# python3
import sys

def InverseBWT(bwt):
    # write your code here
    result = ''
    seen = {}
    new_bwt = []
    for i in bwt:
        if i not in seen:
            seen[i] = 1
        new_bwt.append(i+str(seen[i]))
        seen[i] += 1
    new_bwt_sorted = sorted(new_bwt, key=lambda x: (x[0], int(x[1:])))
    look = dict(zip(new_bwt, new_bwt_sorted))
    key = '$1'
    for _ in bwt:
        key = look[key]
        result += key[0]
    return result


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))