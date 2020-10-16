#!/usr/bin/python3

import sys, threading, math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  last = -math.inf
  stack = []
  i = 0
  while True:
      if i != -1:
          stack.append(i)
          i = tree[i][1]
      elif bool(stack):
          i = stack.pop()
          if last > tree[i][0]:
            return False
          last = tree[i][0]
          i = tree[i][2]
      else:
          break
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #print(tree)
  if nodes == 0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
