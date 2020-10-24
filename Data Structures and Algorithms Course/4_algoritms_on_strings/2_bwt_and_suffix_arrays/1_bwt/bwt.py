# python3
import sys

def BWT(text):
    n = len(text)
    array = sorted([text[i:n] + text[0:i] for i in range(n)])
    return ''.join([val[-1] for val in array])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))