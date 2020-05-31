# python3
import sys

def BWT(text):
    array = []
    res = ''
    n = len(text)
    for i in range(len(text)):
        array.append(text[i:n] + text[0:i])
    array.sort()
    for val in array:
        res += val[-1]
    return res

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))