# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = 256
    pat_len = len(pattern)
    t_len = len(text)
    result = []
    p_hash = poly_hash(pattern, p, x)
    h = precompute_hashes(text, t_len, pat_len, p, x)
    for i in range(t_len - pat_len + 1):
        if p_hash != h[i]:
            continue
        if pattern == text[i:i+pat_len]:
            result.append(i)

    return result

def poly_hash(string, p, x):
    hash_value = 0
    for i in range(len(string)-1, -1, -1):
        hash_value = (((hash_value * x + ord(string[i])) % p) + p) % p
    return hash_value


def precompute_hashes(text, t_len, pat_len, p, x):
    h = [0] * (t_len - pat_len +1)
    s = text[(t_len-pat_len):]
    h[t_len - pat_len] = poly_hash(s, p, x)
    y = 1
    for _ in range(pat_len):
        y = (((y * x) % p) + p) % p
    for i in range(t_len - pat_len -1, -1, -1):
        h[i] = (((x * h[i+1] + ord(text[i]) - y * ord(text[i + pat_len])) % p) + p) % p
    return h


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

