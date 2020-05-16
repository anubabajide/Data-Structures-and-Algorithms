#Solution function, takes in a Binary Tree Node and returns a List of Items in the Tree traversed post-order
def postorderTraversal(root: TreeNode) -> List[int]:
	#array to store the items
	array=[]
	#recursive call
	return dummy(root,array)

def dummy(root, array):
	#check if there is an item in the node
	if root is not None:
		#Left node first
		dummy(root.left, array)
		#Right node second
		dummy(root.right, array)
	    	#Parent Node last
		array.append(root.val)
	return array
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
