# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))

        if next in ")]}":
            if bool(opening_brackets_stack) is False:
                return (i+1)
            temp = opening_brackets_stack.pop()[0]
            if (temp=='(' and next ==')') or (temp=='[' and next ==']') or (temp=='{' and next =='}'):
                continue
            return (i+1)
    if bool(opening_brackets_stack) is True:
        return opening_brackets_stack.pop()[1] +1
    return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
