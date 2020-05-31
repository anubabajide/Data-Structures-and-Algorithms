# python3

import sys
import random


class Vertex:
	def __init__(self, key, rank, left, right, parent, position):
		(self.key, self.rank, self.left, self.right, self.parent, self.pos) = (key, rank, left, right, parent, position)

def update(v):
	if v == None:
		return
	v.rank = 1 + (v.left.rank if v.left != None else 0) + (v.right.rank if v.right != None else 0)
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
		order = get_order(v)
		if order >= key and (next == None or order < get_order(next)):
			next = v
		last = v
		if order == key:
			break
		if order < key:
			v = v.right
		else:
			v = v.left
	root = splay(last)
	return (next, root)

def find2(root, key):
	v = root
	last = root
	next = None
	while v != None:
		if v.pos >= key and (next == None or v.pos < next.pos):
			next = v
		last = v
		if v.pos == key:
			break
		if v.pos < key:
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

def split2(root, key):
	(result, root) = find2(root, key)
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

def insert(x, rank):
	global root
	(left, right) = split2(root, rank)
	new_vertex = Vertex(x, rank, None, None, None, rank)
	root = merge(merge(left, new_vertex), right)
	
def get_order(node):
	r = node.left.rank if node.left else 0
	prev = node
	node = node.parent
	while node:
		if node.right == prev:
			r += 1
			r += (node.left.rank if node.left else 0)
		prev = node
		node = node.parent
	return r
	

def inOrder(root):
	stack = []  
	res = []
	# res1 = []
	# res2 = []
	while stack or root: 
		if root is not None: 
			stack.append(root)
			root = root.left
		elif(stack):
			root = stack.pop()
			res.append(root.key)
			# res1.append(str(get_order(root)))
			# res2.append(str(root.rank))
			root = root.right
		else:
			break
	return ''.join(res)#, ' '.join(res1), ' '.join(res2)

class Rope:
	def __init__(self, s):
		self.s = s
		for i in random.sample(list(range(len(self.s))), k = len(self.s)):
			insert(self.s[i], i+1)
		global root
		# print(inOrder(root))
		
	def result(self):
		global root
		return inOrder(root)

	def process(self, i, j, k):
		global root
		left, middle = split(root, i)
		middle, right = split(middle, j-i+1)
		root = merge(left, right)
		left, right = split(root, k)
		root = merge(merge(left, middle), right)

# Write your code here
								

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
	
print(rope.result())
