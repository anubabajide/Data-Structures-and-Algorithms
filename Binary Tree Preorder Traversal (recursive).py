#Solution function, takes in a Binary Tree Node and returns a List of Items in the Tree traversed pre-order 
def preorderTraversal(root: TreeNode) -> List[int]:
	#array to store the items
	array=[]
	#recursive call on the
	return dummy(root,array)

def dummy(root, array):
	#check if there is an item in the node
	if root is not None:
		#Parent Node first
		array.append(root.val)
		#Left node second
		dummy(root.left, array)
		#Right node last
		dummy(root.right, array)
	return array

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
