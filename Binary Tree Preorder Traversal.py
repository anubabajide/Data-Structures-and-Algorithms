# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#Recursive Solution
    def dummy(self, root, array):
        if root is not None:
            array.append(root.val)
            self.dummy(root.left, array)
            self.dummy(root.right, array)
        return array
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        array=[]
        return self.dummy(root,array)

#Iterative Solution
	# def preorderTraversal(self, root: TreeNode) -> 'List[int]':
		# rst = []
		# stack = []
		# while root or stack:
			# if root:
				# rst.append(root.val)
				# stack.append(root)
				# root = root.left
			# else:
				# root = stack.pop().right
		# return rst