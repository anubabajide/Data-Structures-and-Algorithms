# python3
import sys

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  # Implement this function yourself
  trie = {0:{}}
  node = 1
  n = len(text)
  for i in range(n):
    nex = 0
    j = i
    while j < n:
      match = sub_fin = text_fin = False
      for val in trie[nex]:
        length, point_to = trie[nex][val]
        pos = val
        if text[j] == text[pos]: 
          match = True
          cur = nex
          nex = point_to
          while text[j] == text[pos]:
            # Keep on checking matching characters till either
            # 1. there is a mismatch
            # 2. Text ends for either of the compared values
            j += 1
            pos += 1
            if (j >= n) or (pos >= length):
              if (j >= n):
                sub_fin = True
              if (pos >= length):
                text_fin = True
              break
          break
      if not match:
        trie[nex][j] = (n, node)
        trie[node] = {}
        node += 1
        break
      else:
        if not (sub_fin or text_fin):
          trie[cur][val] = (pos, node)
          trie[node] = {}
          trie[node][pos] = (length, nex)
          nex = node
          node += 1
        
  # {0:{'A':1,'T':2},1:{'C':3}}
  # print(trie)
  for node in trie:
    for c in trie[node]:
      result.append(text[c:trie[node][c][0]])
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))