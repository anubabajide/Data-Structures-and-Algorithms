# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    #print(self.key, self.left, self.right, end='\n')

  def inOrder(self):
    self.result = []
    stack = []
    i = 0
    while True:
        if i != -1:
            stack.append(i)
            i = self.left[i]
        elif bool(stack):
            i = stack.pop()
            self.result.append(self.key[i])
            i = self.right[i]
        else:
            break
    return self.result

  def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

  def preOrder(self):
    self.result = []
    stack = []
    i = 0
    while i != -1 or bool(stack):
        if i != -1:
            self.result.append(self.key[i])
            stack.append(i)
            i = self.left[i]
        else:
            i = self.right[stack.pop()]
    return self.result

  def postOrder(self):

    self.result = []
    stack=[]
    i =0
    while i != -1 or bool(stack):
        while i != -1:
            if self.right[i] != -1:
                stack.append(self.right[i])
            stack.append(i)
            i = self.left[i]
        i = stack.pop()
        if (self.right[i] != -1 and self.peek(stack) == self.right[i]):
            stack.pop()
            stack.append(i)
            i = self.right[i]
        else:
            self.result.append(self.key[i])
            i = -1
                
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
