def peek(stack): 
	if len(stack) > 0: 
		return stack[-1] 
	return None

def postorderTraversal(root: TreeNode) -> List[int]:
	stack=[]
	res = []
	
	while True:
	
		#get to the left-most node
		while root: 
			#check if a right node exists for the left node and append it if so
			if root.right is not None: 
				stack.append(root.right) 
			
			#append the parent node for future traversal
			stack.append(root) 
			#update root to find left-most node
			root = root.left 

		#get left-most node
		root = stack.pop() 

		#there is no left child node, check if there is any right child node 
		if (root.right is not None and peek(stack) == root.right): 
			#remove the right child node from the stack, append the parent node and continue traversal from the right child node
			stack.pop()   
			stack.append(root) 
			root = root.right 

		#if there are no left and right child nodes, the current node is the left-most, 
		#append it and delete  
		else: 
			res.append(root.val)  
			root = None

		#check if the stack is empty and terminate
		if (len(stack) <= 0): 
			break
	return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
