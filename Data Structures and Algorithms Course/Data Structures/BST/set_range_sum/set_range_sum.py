# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

  
# Code that uses splay tree to solve the problem
                                    
root = None


def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  
def erase(x):
  global root
  # Implement erase yourself
  targ, root = find(root, x)
  if targ is None:
    return
  if targ.key != x:
    return
  targ = splay(targ)
  if targ.right and targ.left:
    temp = targ.right
    while temp:#Find Next Element
      last = temp
      temp = temp.left
    #Splay Next Element to bring it to top
    next = splay(last)
    del last
    temp = next.left
    while temp:#Find Previous Element (target Element)
      last = temp
      temp = temp.right
    del temp
    #Splay target and update pointers
    targ = splay(last)
    l = targ.left
    r = targ.right
    r.left = l
    l.parent = r
    r.parent = None
    root = r
  elif targ.left:
    temp = targ.left
    while temp:#Find Previous element
      last = temp
      temp = temp.right
    del temp
    #Splay Previous Element, target is lone leaf on right subtree
    root = splay(last)
    root.right = None
  elif targ.right:
    temp = targ.right
    while temp:#Find Next Element
      last = temp
      temp = temp.left
    #Splay Next Element to bring it to top
    root = splay(last)
    root.left = None
  else:
    root = None
  return


def search(x): 
  global root
  targ, root = find(root, x)
  if targ is None or targ.key != x:
    return False
  return True
  
def sum(fr, to): 
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0
  if middle:
    ans =  middle.sum
  middle = merge(middle, right)
  root = merge(left, middle)
  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO