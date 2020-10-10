#python3

import os

if __name__ == "__main__":
    folders = [x for x in next(os.walk('.'))[1] if x != '.git' and x != 'Word Search II - Trie']
    def gen():
        f = open('README.md', 'r')
        a = ''
        temp = next(f)
        while temp:
            a += temp 
            if temp == '\n':
                yield a
                a = ''
            temp = next(f)
        f.close()

    dfs = gen()
    print(next(dfs))

    for folder in folders:
        file = open('{}/README.md'.format(folder), 'r+')
        file.write(next(dfs))
        file.close()